# Projeto Previsão do Tempo

Este é um aplicativo simples de previsão do tempo desenvolvido em Python, utilizando a biblioteca `tkinter` para a interface gráfica e a biblioteca `requests` para consumir dados de uma API REST do OpenWeatherMap.

## Funcionalidades

*   Permite ao usuário buscar a previsão do tempo para qualquer cidade.
*   Exibe a temperatura atual, umidade e uma descrição das condições climáticas.

## Requisitos

*   Python 3.x
*   Biblioteca `requests`

## Instalação

1.  **Clone o repositório (ou baixe o código):**

    ```bash
    git clone https://github.com/seu-usuario/projeto-previsao-tempo.git
    cd projeto-previsao-tempo
    ```

2.  **Instale as dependências:**

    ```bash
    pip install requests
    ```

## Configuração da API Key

Para que o aplicativo funcione, você precisará de uma chave de API do OpenWeatherMap. Siga os passos abaixo para obtê-la:

1.  Acesse o site: [https://openweathermap.org/api](https://openweathermap.org/api)
2.  Crie uma conta gratuita ou faça login.
3.  Vá para a seção 'API keys' no seu perfil.
4.  Copie a chave gerada.

Após obter sua chave, abra o arquivo `main.py` e substitua `"CHAVE_API"` pela sua chave real:


## Como Executar

No diretório do projeto, execute o seguinte comando:

```bash
python main.py
```

## Estrutura do Projeto

```
projeto-previsao-tempo/
├── main.py
└── README.md
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades. Para isso, siga os passos:

1.  Faça um fork do repositório.
2.  Crie uma nova branch (`git checkout -b feature/sua-feature`).
3.  Faça suas alterações e commit (`git commit -m 'Adiciona nova feature'`).
4.  Envie para a branch original (`git push origin feature/sua-feature`).
5.  Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.


