# FarmTech Solutions

Aplicação desenvolvida para gestão de plantios e análise estatística de dados agrícolas, como parte do projeto da disciplina de tecnologia da FIAP.

## Arquivos

- `farmtech.py` — sistema de cadastro de plantios em Python, com cálculo de área e manejo de insumos
- `farmtech.R` — análise estatística dos dados de plantio (média, desvio padrão, mínimo, máximo e total)
- `farmtech_clima.R` — conexão com API meteorológica pública para exibir dados climáticos de Campinas-SP e recomendar condições de manejo
- `resumo_embrapa.docx` — resumo do artigo "Uso de VANTs em Agricultura de Precisão" da Embrapa

## Tecnologias

- Python 3
- R / RStudio
- API Open-Meteo (gratuita, sem chave)

## Como rodar

**Python:**
```bash
python farmtech.py
```

**R — estatísticas:**
Abra `farmtech.R` no RStudio e clique em **Source**

**R — clima:**
Abra `farmtech_clima.R` no RStudio e clique em **Source**
> Na primeira execução instala os pacotes `httr` e `jsonlite` automaticamente
