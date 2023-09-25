
## Importação de Pacotes
import time
from datetime import datetime
from pyModbusTCP import client
from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils


# Manipulação de float 
class FloatModbusClient(ModbusClient):
    def read_float(self, address, number=1):
        reg_l = self.read_holding_registers(address, number * 2)
        if reg_l:
            return [
                utils.decode_ieee(f) for f in utils.word_list_to_long(reg_l)
            ]
        else:
            return None


def run_client():
   
    # Ler dados
    m = FloatModbusClient(
        host='localhost',
        port=502,
        auto_open=True
    ) 

    # informação de horas enviadas pelo servidor
    hora = str(m.read_holding_registers(4,1)[0]) + str(m.read_holding_registers(5,1)[0]) + str(m.read_holding_registers(6,1)[0])
    hora = datetime.fromtimestamp(float(hora))
    print(hora, end=' -> ')

    # dados
    print(*m.read_holding_registers(1,1), end=' | ')
    print(*m.read_holding_registers(2,1), end=' | ')
    print(*m.read_holding_registers(3,1))

    # fecha conexão Modbus
    m.close()



print('Iniciando coleta de dados...')
while True:

    try:
        run_client()
    except Exception as e:
        print(e)
        break

    # Tempo de amostragem
    time.sleep(5) # 5s

print('Fim da coleta de dados')