# FarmTech Solutions - dados climáticos de Campinas-SP
# API usada: Open-Meteo (gratuita, sem precisar de chave)
# util pra fazenda porque temperatura e chuva afetam direto
# a decisão de quando aplicar herbicida ou fertilizante

# precisamos desses dois pacotes pra fazer requisição e ler o JSON
# instala só na primeira vez que rodar
install.packages("httr")
install.packages("jsonlite")

library(httr)
library(jsonlite)

# coordenadas de Campinas-SP
lat <- -22.9056
lon <- -47.0608

# monta a URL da API com os dados que queremos
# temperature_2m = temperatura a 2m do chão (padrão meteorológico)
# precipitation = chuva em mm
# windspeed_10m = vento a 10m do chão
url <- paste0(
  "https://api.open-meteo.com/v1/forecast",
  "?latitude=", lat,
  "&longitude=", lon,
  "&current_weather=true",
  "&hourly=temperature_2m,precipitation,windspeed_10m,relativehumidity_2m",
  "&forecast_days=1"
)

# faz a requisição
resposta <- GET(url)

# verifica se deu certo
if (status_code(resposta) == 200) {

  # converte o JSON pra lista do R
  dados <- fromJSON(content(resposta, as = "text", encoding = "UTF-8"))

  # pega os dados atuais
  clima_atual <- dados$current_weather

  # pega médias do dia dos dados por hora
  temp_media  <- mean(dados$hourly$temperature_2m)
  chuva_total <- sum(dados$hourly$precipitation)
  umid_media  <- mean(dados$hourly$relativehumidity_2m)
  vento_medio <- mean(dados$hourly$windspeed_10m)

  print("=== FARMTECH - CLIMA CAMPINAS-SP ===")

  print("-- Agora --")

  print("Temperatura (°C):")
  print(clima_atual$temperature)

  print("Velocidade do vento (km/h):")
  print(clima_atual$windspeed)

  print("-- Previsão do dia --")

  print("Temperatura média (°C):")
  print(round(temp_media, 1))

  print("Chuva total prevista (mm):")
  print(round(chuva_total, 1))

  print("Umidade média (%):")
  print(round(umid_media, 1))

  print("Vento médio (km/h):")
  print(round(vento_medio, 1))

  # dica de manejo baseada nos dados
  # chuva acima de 5mm = não aplicar insumo (vai ser lavado)
  # vento acima de 20km/h = não pulverizar (deriva do produto)
  print("-- Recomendação de manejo --")

  if (chuva_total > 5) {
    print("Chuva prevista acima de 5mm - evitar aplicação de insumos hoje")
  } else if (vento_medio > 20) {
    print("Vento acima de 20km/h - risco de deriva na pulverização")
  } else {
    print("Condições favoráveis para aplicação de insumos")
  }

} else {
  print("Erro ao conectar na API - verifique sua internet")
  print(status_code(resposta))
}
