from generate_cli import initialize_model, evaluate_instruction
import time
import socket


# Initialisation du modèle
initialize_model(
    load_8bit=False, 
    base_model="/var/llama/llama-7b-hf/",
    lora_weights="/var/llama/alpaca-lora/Demo_Video_ExpansIA/"
)

# Fonction pour gérer la demande et renvoyer la réponse
"""
def old_handle_request(request):
    instructions = [request]
    responses = []
    for instruction in instructions:
        start = time.time()
        real_instruction = "Réponds à la question sur la document : Transformation de vos documents en IA conversationnelle (Rédigé le 30/06/2023 par le CEO d'ExpansIA Vincent RYCKBOSCH)"
        responses += evaluate_instruction(real_instruction, input=instruction)
        print("Instruction:", instruction)
        for response in responses:
            print("Response:", response)
        print("Time:", time.time() - start)
        print()
    return responses
"""

# Fonction pour gérer la demande et renvoyer la réponse
def handle_request(request):
    start = time.time()
    instruction = "Réponds à la question sur le document : Transformation de vos documents en IA conversationnelle (Rédigé le 30/06/2023 par le CEO d'ExpansIA Vincent RYCKBOSCH)"
    response = evaluate_instruction(instruction=instruction, input=request)
    print("Instruction:", instruction)
    print("Input:", request)
    print("Response:", response)
    print("Time:", time.time() - start)
    print()
    return response


# Configuration du serveur
host = 'localhost'  # Adresse IP du serveur (ou '' pour toutes les interfaces)
port = 1234  # Port à utiliser

# Création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du socket à l'adresse et au port spécifiés
server_socket.bind((host, port))

# Mise en écoute du socket
server_socket.listen(1)

print(f"Le serveur écoute sur le port {port}...")

while True:
    # Attente d'une connexion entrante
    client_socket, addr = server_socket.accept()
    print(f"Connexion entrante de {addr}")

    # Réception des données du client
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Données reçues : {data}")

    # Traitement de la demande et envoi de la réponse
    response = handle_request(data)

    # Envoi de la réponse au client
    client_socket.sendall(str(response).encode('utf-8'))

    # Fermeture de la connexion
    client_socket.close()
