import assert from 'node:assert/strict';
import fs from 'node:fs';

const indexHtml = fs.readFileSync('index.html', 'utf8');
const scriptJs = fs.readFileSync('script.js', 'utf8');

assert.ok(indexHtml.includes('Portfolio'), 'index.html should contain Portfolio title text');
assert.ok(indexHtml.includes('id="projects"'), 'index.html should include projects section');
assert.ok(scriptJs.includes('const projects = ['), 'script.js should define projects array');
