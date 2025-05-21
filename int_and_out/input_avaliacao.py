def inputar_contexto():
    print("Informe os dados do contexto (pressione Enter para deixar em branco):")
    contexto = {}

    cod = input("Código(s) da infração (separados por vírgula): ").strip()
    if cod:
        contexto["cod"] = cod

    prova = input("Há provas? (True/False): ").strip().lower()
    if prova in ["true", "false"]:
        contexto["prova"] = prova == "true"

    intencao = input("Houve intenção? (True/False): ").strip().lower()
    if intencao in ["true", "false"]:
        contexto["intencao"] = intencao == "true"

    privado = input("Ocorreu em ambiente privado? (True/False): ").strip().lower()
    if privado in ["true", "false"]:
        contexto["privado"] = privado == "true"

    reincidencia = input("É reincidência? (True/False): ").strip().lower()
    if reincidencia in ["true", "false"]:
        contexto["reincidencia"] = reincidencia == "true"

    return contexto
