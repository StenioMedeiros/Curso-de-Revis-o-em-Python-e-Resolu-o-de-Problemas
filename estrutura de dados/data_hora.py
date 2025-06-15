# =====================================================
# Manipulação de Datas, Horas e Fuso Horário com datetime
# =====================================================

from datetime import date, time, datetime, timedelta, timezone

# ---------------------------
# Datas com date
# ---------------------------
data = date(2023, 10, 1)
print(f"\n[Data específica] -> {data}")  # Data: 2023-10-01
print(f"[Data de hoje com .today()] -> {date.today()}")  # Exibe a data atual do sistema

# ---------------------------
# Horas com time
# ---------------------------
hora = time(15, 30, 45)
print(f"\n[Hora específica] -> {hora}")  # Hora: 15:30:45

# ---------------------------
# Datas e Horas com datetime
# ---------------------------
data_hora = datetime(2023, 10, 1, 15, 30, 45, 12)
print(f"\n[Data e Hora específica] -> {data_hora}")  # Data e Hora: 2023-10-01 15:30:45.000012

print(f"\n[Data e Hora atual] -> {datetime.now()}")  # Exibe o momento atual
print(f"[Data e Hora atual formatada] -> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")  # Formatação personalizada


# ---------------------------
# Previsão de Conclusão com timedelta
# ---------------------------
tipo_carro = 'Ferrari'
tempo_ferrari = datetime.now() + timedelta(hours=2, minutes=30, seconds=45)
print(f"\n[Previsão de conclusão da lavagem - {tipo_carro}] -> {tempo_ferrari}")

tempo_lamborghini = datetime.now() + timedelta(hours=3, minutes=15, seconds=30)
print(f"[Previsão de conclusão da lavagem - Lamborghini] -> {tempo_lamborghini}")


# ---------------------------
# Conversão e Formatação com strftime() e strptime()
# ---------------------------
data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"

mascara_ptbr = "%d/%m/%Y %a"  # Exemplo: 20/10/2023 Sex
mascara_en = "%Y-%m-%d %H:%M"  # Para parsear string no formato EN

print(f"\n[Data atual formatada - estilo pt-BR] -> {data_hora_atual.strftime(mascara_ptbr)}")

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(f"[String convertida para datetime] -> {data_convertida}")
print(f"[Tipo da variável convertida] -> {type(data_convertida)}")


# ---------------------------
# Trabalhando com Fuso Horário (timezone)
# ---------------------------
data_oslo = datetime.now(timezone(timedelta(hours=2)))      # UTC+2
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))  # UTC-3

print(f"\n[Data e Hora em Oslo (UTC+2)] -> {data_oslo}")
print(f"[Data e Hora em São Paulo (UTC-3)] -> {data_sao_paulo}")
