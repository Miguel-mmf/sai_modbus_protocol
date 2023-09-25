'''
Esse servidor envia os dados para o cliente Modbus
'''

import pytz
import random # estou gerando valores de maneira aleatória
from time import sleep
from datetime import datetime
from pyModbusTCP.server import DataBank, ModbusServer


class ServidorMODBUS(): 
    """
    Classe Servidor Modbus
    """

    def __init__(self, host_ip, port):
        """
        Construtor
        """
        self._server = ModbusServer(
            host=host_ip,
            port=port,
            no_block=True
        )

    def run_server(self):
        """
        Execução do servidor Modbus
        """
        try:

            self._server.start() #aqui o servidor já está atendendo os clientes
            print("Servidor Modbus em execução")
            while True:
                # j = 0
                while True:
                    # hora = pd.DataFrame(data.datetime.astype(str))
                    hora = pytz.timezone('America/Fortaleza').localize(
                        datetime.utcnow()
                    )
                    print(hora, end =' -> ')
                    hora = str(datetime.timestamp(hora))
                    h1 = [(hora[:4])]
                    h2 = [(hora[4:8])]
                    h3 = [(hora[8:10])]

                    _aux = [random.randint(0,100),random.randint(0,100),random.randint(0,100)]
                    self._server.data_bank.set_holding_registers(1,[_aux[0]])
                    self._server.data_bank.set_holding_registers(2,[_aux[1]])
                    self._server.data_bank.set_holding_registers(3,[_aux[2]])
                    self._server.data_bank.set_holding_registers(4,h1)
                    self._server.data_bank.set_holding_registers(5,h2)
                    self._server.data_bank.set_holding_registers(6,h3)
                    
                    print(_aux[0], end=' | ')
                    print(_aux[1], end=' | ')
                    print(_aux[2])
                    sleep(5) # também de 5 em 5 segundos

        except Exception as e:
            print("Erro: ",e.args)


if __name__ == "__main__":
    
    servidor = ServidorMODBUS(
        host_ip="localhost",
        port=502
    )
    servidor.run_server()