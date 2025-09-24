#Timedelta = (semana, hora, minutos, segunods...)

from datetime import timedelta,datetime

print("-=-"*15)
print("LAVA-RÁPIDO")
print("-=-"*15)

horario_atual = datetime.now() #Pode usar ou o .today() ou também o .utcnow()

tamanho_veiculo = input("Informe o tamanho do seu veículo [P,M ou G]:").upper()

tempo_veiculo_pequeno = 30
tempo_veiculo_medio = 45
tempo_veiculo_grande = 60

if tamanho_veiculo == "P":
    horario_de_retirada = horario_atual + timedelta(minutes=tempo_veiculo_pequeno)
    print(f"Horário de chegada: {horario_atual} \nRetire seu veículo em: {horario_de_retirada}")
    
elif tamanho_veiculo == "M":
    horario_de_retirada = horario_atual + timedelta(minutes=tempo_veiculo_medio)
    print(f"Horário de chegada: {horario_atual} \nRetire seu veículo em: {horario_de_retirada}")
    
else:
    horario_de_retirada = horario_atual + timedelta(minutes=tempo_veiculo_grande)
    print(f"Horário de chegada: {horario_atual} \nRetire seu veículo em: {horario_de_retirada}")