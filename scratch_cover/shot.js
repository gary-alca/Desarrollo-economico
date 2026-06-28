const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
  await p.goto('file://' + __dirname + '/cover.html');
  await p.screenshot({ path: 'caratula_beca18.png' });
  await b.close();
})();
