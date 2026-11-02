from django.shortcuts import render
from .agent import ask_agent


def chat_view(request):
    answer = None
    message = ""

    if request.method == "POST":
        message = request.POST.get("message", "").strip()

        if message:
            try:
                answer = ask_agent(message)
            except Exception as error:
                answer = f"Error: {error}"

    return render(
        request,
        "chat/chat.html",
        {
            "message": message,
            "answer": answer,
        },
    )