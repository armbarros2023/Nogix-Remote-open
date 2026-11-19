// Visual do Nogix Remote (cores e peças da tela inicial), copiado do
// theme.css/styles.css do NOGIX v0.3. Só aparência: as ações continuam
// nas páginas originais do RustDesk.
import 'package:flutter/material.dart';
import 'package:flutter_hbb/common.dart';
import 'package:flutter_hbb/desktop/pages/desktop_tab_page.dart';
import 'package:flutter_hbb/models/platform_model.dart';
import 'package:get/get.dart';

class NogixColors {
  NogixColors._();

  static const topbar = Color(0xFF081323);
  static const topbarDark = Color(0xFF060F1D);
  static const topbarLine = Color(0xFF1B314A);
  static const markA = Color(0xFF2686FF);
  static const markB = Color(0xFF0647BC);
  static const primary = Color(0xFF1769ED);
  static const primaryB = Color(0xFF3287F1);
  static const teal = Color(0xFF106C7B);
  static const recentA = Color(0xFF0B1728);
  static const recentB = Color(0xFF10233A);
  static const badgeBg = Color(0xFFF7E8B4);
  static const badgeInk = Color(0xFF61470D);

  static bool _dark(BuildContext c) => Theme.of(c).brightness == Brightness.dark;
  static Color canvas(BuildContext c) =>
      _dark(c) ? const Color(0xFF07111F) : const Color(0xFFEDF2F8);
  static Color ink(BuildContext c) =>
      _dark(c) ? const Color(0xFFE8F1FC) : const Color(0xFF16243A);
  static Color muted(BuildContext c) =>
      _dark(c) ? const Color(0xFF9AADC3) : const Color(0xFF64758D);
  static Color field(BuildContext c) =>
      _dark(c) ? const Color(0xFF0D1B2D) : Colors.white;

  /// Cartão "Este computador" (azul) e "Acessar outro computador" (verde-água).
  static BoxDecoration localCard(BuildContext c) => _card(
      c,
      _dark(c)
          ? const [Color(0xFF0F2440), Color(0xFF0D1B2D)]
          : const [Color(0xFFDCECFF), Color(0xFFF2F8FF)],
      _dark(c) ? const Color(0xFF2A5D96) : const Color(0xFF83B8ED));
  static BoxDecoration remoteCard(BuildContext c) => _card(
      c,
      _dark(c)
          ? const [Color(0xFF0C2A2E), Color(0xFF0D1B2D)]
          : const [Color(0xFFDCF2F1), Color(0xFFF1FAF9)],
      _dark(c) ? const Color(0xFF2A7D84) : const Color(0xFF79C2C7));

  static BoxDecoration _card(BuildContext c, List<Color> g, Color border) =>
      BoxDecoration(
        gradient: LinearGradient(
            colors: g, begin: Alignment.topLeft, end: Alignment.bottomRight),
        border: Border.all(color: border),
        borderRadius: BorderRadius.circular(14),
      );

  static const recentSection = BoxDecoration(
    gradient: LinearGradient(
        colors: [recentA, recentB],
        begin: Alignment.topLeft,
        end: Alignment.bottomRight),
    borderRadius: BorderRadius.all(Radius.circular(16)),
  );
}

/// Marca do NOGIX: o "N" com dois pontos, num quadrado azul.
class NogixMark extends StatelessWidget {
  final double size;
  const NogixMark({Key? key, this.size = 34}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final r = Radius.circular(size * 0.3);
    return Container(
      width: size,
      height: size,
      decoration: BoxDecoration(
        gradient: const LinearGradient(
            colors: [NogixColors.markA, NogixColors.markB],
            begin: Alignment.topLeft,
            end: Alignment.bottomRight),
        borderRadius: BorderRadius.only(
            topLeft: r,
            topRight: r,
            bottomRight: r,
            bottomLeft: Radius.circular(size * 0.08)),
      ),
      child: CustomPaint(painter: _MarkPainter()),
    );
  }
}

class _MarkPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size s) {
    // Desenho em grade 36x36, igual ao SVG do site.
    final k = s.width / 36;
    final line = Paint()
      ..color = Colors.white
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3.4 * k
      ..strokeCap = StrokeCap.round
      ..strokeJoin = StrokeJoin.round;
    final path = Path()
      ..moveTo(8 * k, 26 * k)
      ..lineTo(8 * k, 10 * k)
      ..lineTo(28 * k, 26 * k)
      ..lineTo(28 * k, 10 * k);
    canvas.drawPath(path, line);
    final dot = Paint()..color = Colors.white;
    canvas.drawCircle(Offset(8 * k, 10 * k), 3 * k, dot);
    canvas.drawCircle(Offset(28 * k, 26 * k), 3 * k, dot);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}

/// Barra superior: marca, Configurações e Claro/escuro.
class NogixTopBar extends StatelessWidget {
  const NogixTopBar({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final dark = Theme.of(context).brightness == Brightness.dark;
    return Container(
      height: 60,
      padding: const EdgeInsets.symmetric(horizontal: 24),
      decoration: BoxDecoration(
        color: dark ? NogixColors.topbarDark : NogixColors.topbar,
        border:
            const Border(bottom: BorderSide(color: NogixColors.topbarLine)),
      ),
      child: Row(children: [
        const NogixMark(),
        const SizedBox(width: 10),
        Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: const [
            Text('NOGIX',
                style: TextStyle(
                    color: Color(0xFFF4F8FF),
                    fontSize: 18,
                    fontWeight: FontWeight.w800,
                    height: 1.05)),
            Text('REMOTE',
                style: TextStyle(
                    color: Color(0xFF8DB8F0),
                    fontSize: 9.5,
                    letterSpacing: 2.4,
                    fontWeight: FontWeight.w600)),
          ],
        ),
        const Spacer(),
        if (!bind.isDisableSettings())
          _TopButton(
            icon: Icons.tune_rounded,
            label: translate('Settings'),
            onTap: DesktopTabPage.onAddSetting,
          ),
        _TopButton(
          icon: Icons.contrast_rounded,
          label: translate('Theme'),
          onTap: () => MyTheme.changeDarkMode(
              dark ? ThemeMode.light : ThemeMode.dark),
        ),
      ]),
    );
  }
}

class _TopButton extends StatelessWidget {
  final IconData icon;
  final String label;
  final VoidCallback onTap;
  const _TopButton(
      {required this.icon, required this.label, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return TextButton.icon(
      onPressed: onTap,
      icon: Icon(icon, size: 18, color: const Color(0xFFDCE8F8)),
      label: Text(label,
          style: const TextStyle(
              color: Color(0xFFDCE8F8),
              fontSize: 14,
              fontWeight: FontWeight.w600)),
      style: TextButton.styleFrom(
          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12)),
    ).marginOnly(left: 6);
  }
}

/// Rótulo em caixa alta dos campos (ID, senha, código do outro computador).
class NogixLabel extends StatelessWidget {
  final String text;
  final Color color;
  final Widget? trailing;
  const NogixLabel(this.text,
      {Key? key, this.color = NogixColors.primary, this.trailing})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Row(children: [
      Expanded(
        child: Text(text.toUpperCase(),
            overflow: TextOverflow.ellipsis,
            style: TextStyle(
                color: color,
                fontSize: 11.5,
                letterSpacing: 1.6,
                fontWeight: FontWeight.w700)),
      ),
      if (trailing != null) trailing!,
    ]).marginOnly(bottom: 6);
  }
}

/// Caixa tracejada-clara onde ficam o ID e a senha.
BoxDecoration nogixFieldBox(BuildContext context, Color border) =>
    BoxDecoration(
      color: NogixColors.field(context),
      border: Border.all(color: border.withOpacity(0.55)),
      borderRadius: BorderRadius.circular(10),
    );

/// Botões-pílula de opção (modo de aceite, tipo de conexão).
class NogixChip extends StatelessWidget {
  final String label;
  final bool selected;
  final VoidCallback? onTap;
  final Color color;
  const NogixChip(
      {Key? key,
      required this.label,
      this.selected = false,
      this.onTap,
      this.color = NogixColors.primary})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    final ink = NogixColors.ink(context);
    return Material(
      color: selected ? color.withOpacity(0.12) : NogixColors.field(context),
      shape: StadiumBorder(
          side: BorderSide(
              color: selected ? color : ink.withOpacity(0.18), width: 1.2)),
      child: InkWell(
        customBorder: const StadiumBorder(),
        onTap: onTap,
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 13, vertical: 7),
          child: Row(mainAxisSize: MainAxisSize.min, children: [
            if (onTap != null && selected)
              Icon(Icons.radio_button_checked, size: 15, color: color)
                  .marginOnly(right: 6),
            Text(label,
                style: TextStyle(
                    fontSize: 13,
                    fontWeight: FontWeight.w600,
                    color: selected ? color : ink)),
          ]),
        ),
      ),
    );
  }
}

/// Rodapé: NOGIX, estado do serviço, crédito ao RustDesk e versão.
class NogixFooter extends StatelessWidget {
  final Widget status;
  const NogixFooter({Key? key, required this.status}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.only(left: 24, right: 24),
      child: Row(children: [
        Text('NOGIX',
            style: TextStyle(
                fontWeight: FontWeight.w800,
                fontSize: 15,
                color: NogixColors.ink(context))),
        const SizedBox(width: 8),
        Expanded(child: status),
        // Crédito exigido pela licença AGPL do RustDesk.
        loadPowered(context).marginOnly(top: 0, right: 14),
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
          decoration: BoxDecoration(
              color: NogixColors.badgeBg,
              borderRadius: BorderRadius.circular(6)),
          child: Text(version,
              style: const TextStyle(
                  color: NogixColors.badgeInk,
                  fontSize: 12,
                  fontWeight: FontWeight.w700)),
        ),
      ]),
    );
  }
}
