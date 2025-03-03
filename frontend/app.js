// Função para tratar o login
// document.getElementById('login-form').addEventListener('submit', function(event) {
//     event.preventDefault();
//     const username = document.getElementById('login-username').value;
//     const password = document.getElementById('login-password').value;

//     fetch(`${CONFIG.API_URL}/auth/login`, {  // Usando a variável de ambiente
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ username, senha: password })
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.access_token) {
//             alert('Login bem-sucedido. Token: ' + data.access_token);
//             localStorage.setItem('access_token', data.access_token);
//         } else {
//             alert('Erro no login: ' + JSON.stringify(data));
//         }
//     })
//     .catch(error => alert('Erro ao fazer login: ' + error));
// });

document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    fetch(`${CONFIG.API_URL}/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, senha: password })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw new Error(err.detail); });
        }
        return response.text();  // Pega o token como texto
    })
    .then(token => {
        const blob = new Blob([token], { type: 'text/plain' });
        const url = window.URL.createObjectURL(blob);

        // Criar e acionar um link para download automático
        const a = document.createElement("a");
        a.href = url;
        a.download = "token.txt";
        document.body.appendChild(a);
        a.click();

        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);

        alert("Login bem-sucedido! Token baixado.");
    })
    .catch(error => alert("Erro ao fazer login: " + error.message));
});

// Função para tratar o cadastro
document.getElementById('signup-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('signup-username').value;
    const password = document.getElementById('signup-password').value;

    fetch(`${CONFIG.API_URL}/auth/register`, {  // Usando a variável de ambiente
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

    fetch(`${CONFIG.API_URL}/auth/change_password`, {  // Usando a variável de ambiente
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, senha: currentPassword, nova_senha: newPassword })
    })
    .then(response => response.json())
    .then(data => alert('Senha alterada com sucesso: ' + JSON.stringify(data)))
    .catch(error => alert('Erro ao alterar senha: ' + error));
});
