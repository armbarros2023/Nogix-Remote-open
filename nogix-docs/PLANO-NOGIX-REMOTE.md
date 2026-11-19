# Nogix Remote (base RustDesk 1.5.3): plano de modificações e situação

Pasta do projeto: `C:\Users\ARMANDO\Documents\Projetos Claude Code\Nogix Remote - Open`

O código fica em `rustdesk\`. É o RustDesk 1.5.3 original (commit `95cca3f`, `hbb_common` `fae47e0`), com git próprio: cada fase é um commit. `git log` lista as fases, e `git diff c03eb00` mostra tudo o que mudou em relação ao original.

## Objetivo

O pedido tem só duas mudanças. Todo o resto continua funcionando como no RustDesk:

1. **Nome.** "RustDesk" passa a ser "Nogix Remote" em tudo o que o usuário vê: janelas, textos, instaladores, atalhos, executáveis e pacotes.
2. **Tela inicial.** A tela inicial passa a ser a do Nogix Remote, com o visual do NOGIX v0.3. Por trás, ela usa as mesmas funções do RustDesk.

## Situação

| Fase | Commit | Situação |
|---|---|---|
| 1. Nome interno `NogixRemote` | `ad72d90` | feita |
| 2. Textos visíveis "Nogix Remote" | `29c7fe1` | feita |
| 3. Executáveis e pacotes `nogixremote` | `e0d18d4`, mais o ajuste do MSI em `73646a9` | feita |
| 4. Tela inicial do Nogix Remote | `c24cfc9` | feita |
| 5. Ícones com a marca do NOGIX | `d8c1c9a` | feita |
| 6. Build e testes | `73646a9` | workflow pronto; **falta compilar e testar** |
| 7. Celular e IDs de pacote | — | fora do pedido (opcional) |

O commit `b96f474` não é uma fase. Ele só registra no git as imagens originais do RustDesk que o `.gitignore` deixava de fora; sem elas, o build pelo GitHub falharia.

**Importante:** nada foi compilado ainda. Este ambiente não consegue baixar o Flutter, então os erros de compilação, se existirem, só aparecem no primeiro build (Fase 6). O código Dart novo foi revisado à mão contra as funções que ele usa.

## Decisões de nome

| Onde | Fica | Motivo |
|---|---|---|
| Nome exibido | **Nogix Remote** | é o que foi pedido |
| Nome interno (`APP_NAME`) | **NogixRemote**, sem espaço | o código usa esse nome como nome do processo, da janela, da bandeja, do link e da pasta de instalação; com espaço, quebra no Linux e no Windows |
| Executável Windows | `nogixremote.exe` | na instalação, vira `C:\Program Files\NogixRemote\NogixRemote.exe`, como o RustDesk faz com `RustDesk.exe` |
| Linux | binário `nogixremote`, `/usr/share/nogixremote`, serviço `nogixremote.service`, link `nogixremote://` | segue o nome interno |
| macOS | `NogixRemote.app`; o nome exibido no Finder e no Dock é "Nogix Remote" | o código monta `/Applications/<APP_NAME>.app` |
| Pacotes | `nogixremote-1.5.3-*.deb/.rpm/.msi/.dmg/.exe` | seguem o nome interno |
| Pasta de configuração | `NogixRemote` | fica separada da do RustDesk, então os dois podem conviver no mesmo computador |

### O que não muda

| Item | Motivo |
|---|---|
| Organização `com.carriez` | os scripts de permissão do macOS têm esse prefixo fixo no código; trocar quebra a instalação do serviço no Mac |
| Biblioteca `librustdesk`, crates e módulos Rust | nomes internos de compilação; trocar quebra o build e não muda nada para o usuário |
| `/usr/lib/rustdesk/libdrmtap` (pacote Wayland sem aceite) | o caminho está gravado no binário |
| Endereços rustdesk.com e GitHub do RustDesk | documentação e servidores públicos; a busca de atualização do RustDesk desliga sozinha, porque o nome não é mais RustDesk |
| Chaves das traduções | são identificadores do código; só o texto traduzido mudou |
| Licença AGPL-3.0, copyright e o texto do instalador MSI | obrigação da licença |
| Interface antiga (Sciter), AppImage, Flatpak, Android e iOS | fora do pedido; o workflow só os compila no repositório oficial do RustDesk |

### Crédito ao RustDesk

O crédito aparece no rodapé da tela inicial ("Powered by RustDesk") e na tela Sobre ("Nogix Remote — baseado no RustDesk (AGPL-3.0)").

## Fase 4: tela inicial

| Área | Função do RustDesk usada |
|---|---|
| Barra superior escura: marca N, "NOGIX REMOTE", Configurações e Tema | abre as Configurações; alterna claro/escuro (`MyTheme.changeDarkMode`) |
| Cartão "Este computador": ID e senha de uso único com copiar, atualizar senha, alterar senha e menu ⋮ | `ServerModel`, os mesmos campos da tela antiga |
| Modo de aceite: senha, clique ou ambos | `approve-mode`; quando o app está instalado, abre a página de Segurança, que pede desbloqueio, como nas Configurações |
| Cartão "Controlar computador remoto": campo com autocompletar, Conectar ▾ (incluindo "Pedir aprovação"), Transferir arquivo, Terminal, Túnel TCP, Ver câmera | o mesmo campo e os mesmos menus da tela antiga (`connect()`) |
| Lista de computadores em fundo escuro: Recentes, Favoritos, Na rede, Catálogo, Grupos, busca, grade e ordenação | `PeerTabPage`, sem mudança |
| Rodapé: NOGIX, estado do serviço, crédito e versão | `OnlineStatusWidget`, `loadPowered` e `version` |
| Avisos de instalação, permissões do Mac, Wayland e senha predefinida | os mesmos cartões da tela antiga, agora no topo |

Arquivos alterados:

- **Novo:** `flutter/lib/desktop/widgets/nogix_theme.dart`, com as cores e peças visuais. A marca é desenhada em código, então não há imagem nova no app.
- **`desktop_home_page.dart`:** só o `build()` passa a montar a nova tela. Toda a lógica (`initState`, permissões, atualização) fica igual. Os modos "só recebe" e "só envia" de clientes personalizados continuam com a tela antiga.
- **`connection_page.dart`:** ganhou o parâmetro `nogixLocalCard`. Sem esse parâmetro, nada muda.
- **`common.dart`:** a cor de destaque passou a ser o azul do NOGIX `#1769ED`.
- **`desktop_setting_page.dart`:** ganhou o link de crédito na tela Sobre.

Em janelas com menos de 560 px de altura útil, a tela rola, em vez de esconder a lista de computadores.

## Fase 6: como compilar

O plano é compilar no GitHub Actions, com o workflow do próprio RustDesk adaptado. Os passos estão no `LEIA-ME.md`. O repositório `nogix-engine` não é usado, a seu pedido; o projeto precisa de um repositório próprio (sugestão: `nogix-remote-open`, privado).

## Riscos

| Risco | Cuidado |
|---|---|
| Erro de compilação no Dart novo | aparece no primeiro build; a correção fica restrita aos três arquivos da Fase 4 |
| Renomear o executável quebrar o serviço, a bandeja ou o link | o executável e o nome interno são sempre iguais (`nogixremote`/`NogixRemote`); teste de serviço em cada sistema (`LEIA-ME.md`) |
| A tela nova esconder alguma função da antiga | a tabela da Fase 4 confere item a item |
| Conflito com o RustDesk instalado no mesmo computador | nome, pasta, serviço e link são próprios |
| Licença | o código-fonte modificado deve ser oferecido a quem receber o app (AGPL-3.0) |
