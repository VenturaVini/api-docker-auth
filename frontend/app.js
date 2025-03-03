// Função para tratar o login
document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    fetch('http://localhost:7200/auth/login', {  // Atualizado para a porta 7200
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, senha: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.access_token) {
            alert('Login bem-sucedido. Token: ' + data.access_token);
            // Armazenar o token de autenticação (por exemplo, no localStorage)
            localStorage.setItem('access_token', data.access_token);
        } else {
            alert('Erro no login: ' + JSON.stringify(data));
        }
    })
    .catch(error => alert('Erro ao fazer login: ' + error));
});

// Função para tratar o cadastro
document.getElementById('signup-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('signup-username').value;
    const password = document.getElementById('signup-password').value;

    fetch('http://localhost:7200/auth/register', {  // Atualizado para a porta 7200
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, senha: password })
    })
    .then(response => response.json())
    .then(data => alert('Cadastro bem-sucedido: ' + JSON.stringify(data)))
    .catch(error => alert('Erro no cadastro: ' + error));
});

// Função para tratar a alteração de senha
document.getElementById('change-password-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('change-username').value;
    const currentPassword = document.getElementById('current-password').value;
    const newPassword = document.getElementById('new-password').value;

    fetch('http://localhost:7200/auth/change_password', {  // Atualizado para a porta 7200
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, senha: currentPassword, nova_senha: newPassword })
    })
    .then(response => response.json())
    .then(data => alert('Senha alterada com sucesso: ' + JSON.stringify(data)))
    .catch(error => alert('Erro ao alterar senha: ' + error));
});
