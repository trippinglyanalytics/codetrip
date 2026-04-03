const projects = [
  {
    name: 'Portfolio Deployment',
    description: 'Containerized static app ready for cloud deployment.',
  },
  {
    name: 'CI/CD Pipeline',
    description: 'GitHub Actions workflow with automated build and test steps.',
  },
  {
    name: 'API Integration Starter',
    description: 'Scaffold ready for environment-based backend integration.',
  },
];

const projectList = document.querySelector('#project-list');

for (const project of projects) {
  const card = document.createElement('article');
  card.className = 'project-card';
  card.innerHTML = `<h4>${project.name}</h4><p>${project.description}</p>`;
  projectList.appendChild(card);
}

document.querySelector('#year').textContent = new Date().getFullYear();
