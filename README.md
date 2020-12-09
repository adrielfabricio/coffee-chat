[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/adrielfabricio/coffee-chat/">
    <img src="./img/logo_2.png" alt="Logo" width="100">
  </a>

  <h3 align="center">Projeto Coffee-Chat</h3>

  <p align="center">
    Projeto desenvolvido para matéria de Redes 1
    <br />
    <a href="https://adrielfabricio.github.io/coffee-chat/"><strong>Documentação do código do projeto</strong></a>
    
    
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Sumário</summary>
  <ol>
    <li>
        <a href="#sobre-o-projeto">Sobre o projeto</a>
        <ul>
            <li><a href="#motivação">Motivação</a></li>
            <li><a href="#ferramentas">Ferramentas</a></li>
            <li><a href="#pré-requisitos">Pré-requisitos</a></li>
            <li>
              <a href="#instalação">Instalação</a>
              <ul>
                <li><a href="#via-conda">Via Conda</a></li>
                <li><a href="#via-pip">Via Pip</a></li>
                <li><a href="#finalizando-instalação-somente-windows">Finalizando instalação (somente Windows)</a></li>
              </ul>
            </li>
        </ul>
    </li>
    <li>
        <a href="#como-começar">Como começar</a>
        <ul>
            <li><a href="#servidor">Servidor</a></li>
            <li><a href="#clientes">Clientes</a></li>
        </ul>
    </li>
    <li><a href="#protocolo">Protocolo</a></li>
    <li><a href="#contribuidores">Contribuidores</a></li>
  </ol>
</details>

## Sobre o projeto

O projeto é de criação de um chat que conecte diversas pessoas na mesma rede. Ele se chama coffee-chat por nossa paixão por café (exceto Samuel) e por ser nosso melhor companheiro na horas mais tardias enquanto programamos.

O projeto foi testado para plataformas windows 10 e ubuntu 20.04.

### Motivação

Esse projeto originou-se pela curiosidade de compreender como o processo de um chat em real-time funciona, além de aprender como diversos computadores poderiam estar conectados na mesma rede sem que houvesse falha no recebimento e envio de mensagens.

### Ferramentas

Para esse projeto utilizamos o Python e o Conda para conteinerização das depedências.

### Pré-requisitos

Todos os requisitos necessários para rodar o projeto estão especificados no arquivo <a href="https://github.com/adrielfabricio/coffee-chat/blob/main/environment.yml">`environment.yml`</a> localizado no diretório raiz do projeto.

### Instalação

Pode ser feita a instalação das dependências via `conda` ou `pip`.

#### Via Conda

Para instalar via conda é necessária ter a última versão do mesmo. Um tutorial para fazer a instalação corretamente do conda no Windows, macOS ou Linux pode ser acessada <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/install/">aqui</a>.

Após concluir a instalação do conda, basta executar o seguinte comando na CLI:

```shell
conda env create -f environment.yml
```

Feito isso, todas as dependências que estão localizadas no `environment.yml` serão instaladas no ambiente que será criado com o nome `coffee-chat`. Para ativar o ambiente execute o comando a seguir:

```shell
conda activate coffee-chat
```

#### Via Pip

Para instalar o projeto utilizando o pip basta utilizar o arquivo `requiriments.txt` localizado no diretório raiz do projeto. Basta executar o comando a seguir:

```shell
pip install -r requirements.txt
```

A versão do pip utilizada no desenvolvimento do projevo foi a v20.3.

#### Finalizando instalação (somente Windows)

O CoffeeChat oferece recurso de notificação para usuários Windows, para isso é necessário instalar duas bibliotecas, executando o comando que segue:

```shell
pip install pywin32
pip install win10toast
```

## Como começar

O projeto é dividido em servidor e cliente. O servidor conectar e gerencia todas as requisições dos clientes. O cliente se comunica com o servidor mandando mensagens e renderiza o retorno dele.

Para rodar o projeto é preciso iniciar um servidor em um endereço IP na rede que os demais clientes possam acessar. Em seguinda é necessário conectar os clientes com esse IP.

### Servidor

Para iniciar o servidor rode o seguinte comando:

```shell
python server.py
```

Após rodar esse comando irá aparecer a seguinte caixa de texto, basta clicar no texto dela e digitar o IP onde o servidor irá rodar e depois aperta `ENTER`

![server-1](./img/server1.png)
![server-2](./img/server2.png)

Com isso o servidor estará pronto para receber os clientes

### Clientes

Para iniciar um cliente basta abrir outro terminal, caso esteja no mesmo computador do servidor, e rodar o seguinte comando

```shell
python client.py
```

Irá abrir uma caixa semelhante ao do servidor, basta preencher com o IP do seu servidor e depois aperta em `ENTER`

![client-1](./img/client1.png)
![client-1](./img/client2.png)

Em seguida, irá abrir uma nova caixa pedindo para o nome de identificação do usuário

![client-1](./img/client3.png)
![client-1](./img/client4.png)

Após preencher o nome do usuário irá abrir uma janela para o chat:

![client-1](./img/client5.png)

Para testar basta digitar algo e enviar. **Atenção!** o input do chat não aceita caracteres especiais.

![client-1](./img/client6.png)

Para criar um novo chat basta abrir um novo terminar e rodar o comando para rodar o cliente novamente e preencher com os dados do servidor, o mesmo vale para caso esteja testando em outro computador.

Quando um novo usuário entra na rede os usuários já existentes são notificados

![client-1](./img/client7.png)

É possivel conectar diversos usuários ao chat, no windows 10 sempre que tiver uma nova mensagem aparecerá ela na notificação do SO

![client-1](./img/client8.png)

## Protocolo

Para a aplicação enviar e receber mensagens criamos uma estrutura client-server, onde o servidor é responsável por receber mensagens e difundir elas para os clientes conectados. Para comunicação entre o servidor e o cliente usamos o modelo TCP/IP.

<div align="center">
  <img src="./img/protocolo2.png" alt="Logo" width="500">
</div>

O servidor quando roda ele armazena todos os clientes conectados guardando seus IP's e suas portas. A distribuição de mensagem funciona da seguinte forma

- Um cliente manda uma mensagem para o servidor
- O servidor recebe e processa a mensagem
- O servidor envia as mensagens para todos os clientes conectados
- Os clientes conectados mostram a mensagem da tela

Para mais informações de como foi realizado a implementação acesse o [link da documentação](https://adrielfabricio.github.io/coffee-chat/)

## Contribuidores

- [Adriel Fabricio](https://github.com/adrielfabricio)
- [Diêgo Marcelino](https://github.com/marcelinodiego)
- [Henrique Serra](https://github.com/SerraZ3)
- [Samuel Mendonça](https://github.com/Syphoon)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/adrielfabricio/coffee-chat.svg?style=for-the-badge
[contributors-url]: https://github.com/adrielfabricio/coffee-chat/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/adrielfabricio/coffee-chat.svg?style=for-the-badge
[forks-url]: https://github.com/adrielfabricio/coffee-chat/network/members
[stars-shield]: https://img.shields.io/github/stars/adrielfabricio/coffee-chat.svg?style=for-the-badge
[stars-url]: https://github.com/adrielfabricio/coffee-chat/stargazers
[issues-shield]: https://img.shields.io/github/issues/adrielfabricio/coffee-chat.svg?style=for-the-badge
[issues-url]: https://github.com/adrielfabricio/coffee-chat/issues
[license-shield]: https://img.shields.io/github/license/adrielfabricio/coffee-chat.svg?style=for-the-badge
[license-url]: https://github.com/adrielfabricio/coffee-chat/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
