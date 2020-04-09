from datetime import datetime, timezone, timedelta
from pytz import timezone as timezones  # para diferenciar do timezone de datetime

data_e_hora_em_texto = '01/03/2020 11:30:55'
data_e_hora1 = datetime.strptime(data_e_hora_em_texto, '%d/%m/%Y %H:%M:%S')
print(data_e_hora1)
print(data_e_hora1.strftime('%d/%m/%Y %H:%M:%S %p'))
print()

# TRABALHANDO COM HORARIOS /--------------------------------------------------/
data_hora_atual = datetime.now()
data_em_texto = data_hora_atual.strftime('%d/%m/%Y %H:%M:%S %p')
difference = timedelta(hours=-3)
fuso_horario = timezone(difference)
print(data_em_texto)

data_hora_SP = data_hora_atual.astimezone(fuso_horario)
dataSP = data_hora_SP.strftime('%d/%m/%Y %H:%M:%S %p')
print(f'Hora Sao Paulo: {dataSP}')

# AGORA COM PYTZ /--------------------------------------------------/
data_e_hora_atuais = datetime.today()
zona = 'America/New_York'
fuso_hora = timezones(zona)
data_e_hora = data_e_hora_atuais.astimezone(fuso_hora)
data_e_hora_em_texto = data_e_hora.strftime('%d/%m/%Y %H:%M:%S %p')
print(f'{zona}: {data_e_hora_em_texto}')


