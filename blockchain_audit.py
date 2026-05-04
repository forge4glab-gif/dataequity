# =================================================================
# DATAEQUITY SYSTEM - AUDITORIA DE EXTRAÇÃO DE DADOS (COOKIES/WEB)
# PROTECTED UNDER COPYRIGHT KEY: DEQS-2026-V1
# REGISTERED WITH INPI - AUTHOR: VICTOR ROBERTO SERRANONI DA COSTA
# FOCO: RASTREABILIDADE E MONETIZAÇÃO DE FLUXO DE INFORMAÇÕES
# =================================================================
import hashlib
import sys
import json

class DataEquityAuditor:
    def __init__(self):
        self.copyright_key = "DEQS-2026-V1"

    def generate_blockchain_hash(self, data_row):
        """Gera hash SHA-256 para linhas de log genéricas."""
        return hashlib.sha256(data_row.encode()).hexdigest()

    def generate_extraction_hash(self, cookie_data, source_url, timestamp):
        """
        Cria a prova imutável da retirada de informação.
        Cobre captações autorizadas e não autorizadas.
        """
        payload = f"{timestamp}-{source_url}-{cookie_data}"
        return hashlib.sha256(payload.encode()).hexdigest()

if __name__ == "__main__":
    auditor = DataEquityAuditor()
    
    # Se receber argumentos via CLI (PowerShell), processa a linha
    if len(sys.argv) > 1:
        log_line = sys.argv[1]
        # Identifica se é um JSON de cookie ou log comum
        try:
            data = json.loads(log_line)
            if "cookie_data" in data:
                print(auditor.generate_extraction_hash(
                    data["cookie_data"], 
                    data.get("source", "unknown"), 
                    data.get("ts", "0")
                ))
            else:
                print(auditor.generate_blockchain_hash(log_line))
        except:
            print(auditor.generate_blockchain_hash(log_line))