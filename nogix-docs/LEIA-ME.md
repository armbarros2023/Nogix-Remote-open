# Nogix Remote (base RustDesk 1.5.3)

Este é o RustDesk 1.5.3 com duas mudanças: o nome passa a ser **Nogix Remote** e a **tela inicial** passa a ter o visual do NOGIX. Todo o resto (conexão, servidores, segurança, transferência de arquivos, terminal) é o RustDesk original.

- `rustdesk/`: o código-fonte, com git. Cada fase é um commit; `git diff c03eb00` mostra todas as mudanças em relação ao original.
- `PLANO-NOGIX-REMOTE.md`: as decisões e a situação de cada fase.
- `docs/previa/`: a prévia aprovada da tela inicial.
- `docs/icones/`: a marca em SVG, usada para gerar os ícones.

## 1. Compilar (GitHub Actions)

Você não precisa instalar nada no PC. O build leva de 1 a 2 horas na primeira vez.

1. Crie um repositório **privado** no seu GitHub, por exemplo `nogix-remote-open`.
2. Envie o código. No Windows, abra o PowerShell na pasta `rustdesk` e rode:
   ```powershell
   git remote add origin https://github.com/armbarros2023/nogix-remote-open.git
   git push -u origin master
   ```
3. No GitHub, abra **Actions → Flutter Nightly Build → Run workflow**.
4. Ao terminar, os instaladores ficam em **Releases → nightly**:
   - Windows: `nogixremote-1.5.4-x86_64.exe` (portátil/instalador) e `.msi`
   - macOS: `nogixremote-1.5.4-aarch64.dmg` (Apple Silicon) e `-x86_64.dmg` (Intel)
   - Linux: `nogixremote-1.5.4-x86_64.deb`, `.rpm`, `-suse.rpm` e o pacote do Arch

Sem certificados configurados, os instaladores saem **sem assinatura**. O Windows mostra o aviso do SmartScreen ("Mais informações → Executar assim mesmo"). No Mac, abra pelo botão direito → Abrir.

Se algum passo falhar, copie o trecho do erro em **Actions** e me envie. Erros na primeira compilação são esperados, porque o código Dart novo não pôde ser compilado aqui.

## 2. Testes de aceite

Faça os testes em pelo menos um Windows e um segundo computador (Mac ou Linux).

| # | Teste | Esperado |
|---|---|---|
| 1 | Instalar e abrir | a janela e a barra de tarefas mostram "Nogix Remote" e o ícone N azul |
| 2 | Procurar "RustDesk" nas telas | só aparece no crédito do rodapé e em Configurações → Sobre |
| 3 | Tela inicial, tema claro e escuro (botão Tema) | barra escura, cartão azul (ID e senha), cartão verde (conectar), lista escura |
| 4 | ID e senha | aparecem; os botões copiar, atualizar senha e alterar senha funcionam |
| 5 | Modo de aceite (senha / clique / ambos) | quando instalado, abre Configurações → Segurança, que pede desbloqueio |
| 6 | Conectar ao outro computador pelo ID | a sessão abre; mouse e teclado funcionam |
| 7 | Transferir arquivo, Terminal, Túnel TCP, Ver câmera | cada botão abre a função correspondente |
| 8 | Recentes, Favoritos, busca | o computador do teste 6 aparece em Recentes |
| 9 | Reiniciar o computador | o serviço inicia sozinho; o ID fica igual |
| 10 | Link `nogixremote://` (Windows/Linux) | abre o Nogix Remote |
| 11 | Desinstalar | remove o app, o serviço e os atalhos |
| 12 | RustDesk instalado no mesmo computador (opcional) | os dois funcionam separados |

## 3. Pontos de atenção

- **Servidores.** O app usa os servidores públicos do RustDesk, como o original. Para usar o seu servidor, é uma mudança separada (Configurações → Rede, ou fixar no código).
- **Licença.** O RustDesk é AGPL-3.0. Quem receber o Nogix Remote tem direito ao código-fonte modificado; guarde este repositório.
- **Assinatura.** Para o Windows não mostrar aviso, é preciso um certificado de assinatura de código. No Mac, é preciso uma conta Apple Developer.
