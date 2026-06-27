import re

from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe


register = template.Library()


HTML_TAG_RE = re.compile(r"<[a-z][\s\S]*>", re.IGNORECASE)
BULLET_RE = re.compile(r"^(?:[-*•]|\d+\.)\s+(.*)$")


@register.filter
def render_portfolio_text(value):
    if value is None:
        return ""

    text = str(value).strip()
    if not text:
        return ""

    if HTML_TAG_RE.search(text):
        return mark_safe(text)

    lines = [line.rstrip() for line in text.splitlines()]
    output = []
    paragraph = []
    bullets = []

    def flush_paragraph():
        if paragraph:
            output.append(f"<p>{escape(' '.join(paragraph).strip())}</p>")
            paragraph.clear()

    def flush_bullets():
        if bullets:
            items = "".join(f"<li>{escape(item)}</li>" for item in bullets)
            output.append(f"<ul>{items}</ul>")
            bullets.clear()

    for line in lines:
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            flush_bullets()
            continue

        bullet_match = BULLET_RE.match(stripped)
        if bullet_match:
            flush_paragraph()
            bullets.append(bullet_match.group(1))
            continue

        flush_bullets()
        paragraph.append(stripped)

    flush_paragraph()
    flush_bullets()

    return mark_safe("".join(output) if output else f"<p>{escape(text)}</p>")
