const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const dist = path.join(root, 'dist');
const files = ['index.html', 'style.css', 'script.js'];

if (!fs.existsSync(dist)) {
  fs.mkdirSync(dist, { recursive: true });
}

for (const file of files) {
  const source = path.join(root, file);
  const target = path.join(dist, file);

  if (!fs.existsSync(source)) {
    throw new Error(`Missing required source file: ${file}`);
  }

  fs.copyFileSync(source, target);
}

console.log('Build complete. Static files copied to dist/.');
