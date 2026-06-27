from django import forms

from .models import Experience, PortfolioProfile


class RichTextWidget(forms.Textarea):
    class Media:
        css = {"all": ("myinfo/css/rich_text_editor.css",)}
        js = ("myinfo/js/rich_text_editor.js",)

    def __init__(self, attrs=None):
        attrs = attrs or {}
        existing_class = attrs.get("class", "")
        attrs["class"] = f"{existing_class} rich-editor-source".strip()
        attrs.setdefault("rows", 10)
        super().__init__(attrs)


class PortfolioProfileAdminForm(forms.ModelForm):
    class Meta:
        model = PortfolioProfile
        fields = "__all__"
        widgets = {
            "summary": RichTextWidget(attrs={"rows": 8, "placeholder": "Write a short bio with simple formatting."}),
        }


class ExperienceAdminForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = "__all__"
        widgets = {
            "description": RichTextWidget(
                attrs={
                    "rows": 10,
                    "placeholder": "Use bullets, short paragraphs, and bold text for your work details.",
                }
            ),
        }
