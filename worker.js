// ============================================================
// 人类世界生存法则 · Anthropic API 代理 Worker
// 部署到 Cloudflare Workers，在环境变量里设置 ANTHROPIC_API_KEY
//
// 这个 Worker 拿着一把真实的 Anthropic key。ALLOWED_ORIGIN 曾经是 '*'，
// 意味着任何网站的 JS 都能拿它当免费 API 用，账单记在你头上。
// 现在改成白名单，且 fail closed：Origin 不在名单里直接 403，不转发。
// ============================================================

const ALLOWED_ORIGINS = new Set([
  'https://ourword.ai',
  'https://www.ourword.ai',
]);

// 只允许代理消息接口，且限制单次输出，避免被当成通用推理后端。
const MAX_TOKENS_CAP = 2048;

function corsHeaders(origin) {
  return {
    'Access-Control-Allow-Origin': origin,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
    'Vary': 'Origin',
  };
}

function json(obj, status, origin) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { 'Content-Type': 'application/json', ...corsHeaders(origin || 'null') },
  });
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin') || '';
    const allowed = ALLOWED_ORIGINS.has(origin);

    if (request.method === 'OPTIONS') {
      return allowed
        ? new Response(null, { headers: corsHeaders(origin) })
        : new Response(null, { status: 403 });
    }

    if (!allowed) {
      return json({ error: 'Forbidden origin' }, 403, null);
    }

    if (request.method !== 'POST') {
      return json({ error: 'Method Not Allowed' }, 405, origin);
    }

    let body;
    try {
      body = await request.json();
    } catch {
      return json({ error: 'Invalid JSON' }, 400, origin);
    }

    if (typeof body.max_tokens !== 'number' || body.max_tokens > MAX_TOKENS_CAP) {
      body.max_tokens = MAX_TOKENS_CAP;
    }

    let apiRes;
    try {
      apiRes = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': env.ANTHROPIC_API_KEY,
          'anthropic-version': '2023-06-01',
        },
        body: JSON.stringify(body),
      });
    } catch (err) {
      return json({ error: 'Upstream request failed', detail: err.message }, 502, origin);
    }

    return new Response(await apiRes.text(), {
      status: apiRes.status,
      headers: { 'Content-Type': 'application/json', ...corsHeaders(origin) },
    });
  },
};
