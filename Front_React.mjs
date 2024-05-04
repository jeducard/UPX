import React, { useState } from 'Front_React.mjs';
import axios from 'axios';

function App() {
  const [nome, setNome] = useState('');
  const [email, setEmail] = useState('');
  const [celular, setCelular] = useState('');
  const [senha, setSenha] = useState('');
  const [biometria, setBiometria] = useState('');

  const cadastrarUsuario = () => {
    axios.post('cadastrar.sql', {
      nome: nome,
      email: email,
      celular: celular,
      senha: senha
    })
    .then(response => {
      console.log(response.data.mensagem);
    })
    .catch(error => {
      console.error('Erro ao cadastrar usuário:', error);
    });
  }

  const iniciarSessaoBiometria = () => {
    axios.post('cadastrar.sql', {
      id: 1, // ID do usuário
      biometria: biometria
    })
    .then(response => {
      console.log(response.data.mensagem);
    })
    .catch(error => {
      console.error('Erro ao iniciar sessão com biometria:', error);
    });
  }

  return (
    <div>
      <input type="text" placeholder="Nome" value={nome} onChange={(e) => setNome(e.target.value)} />
      <input type="email" placeholder="E-mail" value={email} onChange={(e) => setEmail(e.target.value)} />
      <input type="text" placeholder="Celular" value={celular} onChange={(e) => setCelular(e.target.value)} />
      <input type="password" placeholder="Senha" value={senha} onChange={(e) => setSenha(e.target.value)} />
      <button onClick={cadastrarUsuario}>Cadastrar</button>

      <input type="text" placeholder="Biometria" value={biometria} onChange={(e) => setBiometria(e.target.value)} />
      <button onClick={iniciarSessaoBiometria}>Iniciar Sessão com Biometria</button>
    </div>
  );
}

export default App;
