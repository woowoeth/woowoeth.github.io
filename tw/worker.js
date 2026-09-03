// ============================================================
// 人類世界生存法則 · Anthropic API 代理 Worker
// 部署到 Cloudflare Workers，在環境變量裡設置 ANTHROPIC_API_KEY
//
// 這個 Worker 拿著一把真實的 Anthropic key。ALLOWED_ORIGIN 曾經是 '*'，
// 意味著任何網站的 JS 都能拿它當免費 API 用，賬單記在你頭上。
// 現在改成白名單，且 fail closed：Origin 不在名單裡直接 403，不轉發。
// ============================================================

const ALLOWED_ORIGINS = new Set([
  'https://ourword.ai',
  'https://www.ourword.ai',
]);

// 只允許代理消息接口，且限制單次輸出，避免被當成通用推理後端。
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
