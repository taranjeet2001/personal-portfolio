(function () {
  function createButton(label, command, onClick) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "rich-editor__btn";
    button.textContent = label;
    button.addEventListener("click", onClick || function () {
      document.execCommand(command, false, null);
    });
    return button;
  }

  function syncSource(source, editor) {
    source.value = editor.innerHTML;
  }

  function enhance(source) {
    if (source.dataset.richEditorReady === "true") {
      return;
    }

    source.dataset.richEditorReady = "true";
    source.classList.add("rich-editor-source--hidden");

    const wrapper = document.createElement("div");
    wrapper.className = "rich-editor";

    const toolbar = document.createElement("div");
    toolbar.className = "rich-editor__toolbar";

    const editor = document.createElement("div");
    editor.className = "rich-editor__surface";
    editor.contentEditable = "true";
    editor.dataset.placeholder = source.getAttribute("placeholder") || "Write here...";

    const initialValue = source.value || "";
    if (/<[a-z][\s\S]*>/i.test(initialValue)) {
      editor.innerHTML = initialValue;
    } else {
      editor.innerHTML = initialValue.replace(/\n/g, "<br>");
    }

    toolbar.appendChild(createButton("B", "bold"));
    toolbar.appendChild(createButton("I", "italic"));
    toolbar.appendChild(createButton("U", "underline"));
    toolbar.appendChild(createButton("• List", "insertUnorderedList"));
    toolbar.appendChild(createButton("1. List", "insertOrderedList"));
    toolbar.appendChild(createButton("Link", "createLink", function () {
      const url = window.prompt("Enter a link URL");
      if (url) {
        document.execCommand("createLink", false, url);
      }
    }));
    toolbar.appendChild(createButton("Clear", "removeFormat"));

    editor.addEventListener("input", function () {
      syncSource(source, editor);
    });

    source.form && source.form.addEventListener("submit", function () {
      syncSource(source, editor);
    });

    wrapper.appendChild(toolbar);
    wrapper.appendChild(editor);
    source.parentNode.insertBefore(wrapper, source);
    wrapper.appendChild(source);
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("textarea.rich-editor-source").forEach(enhance);
  });
})();
