# FarmTech Solutions - estatísticas dos plantios

# dados dos plantios
culturas    <- c("Soja", "Milho", "Soja", "Milho", "Soja")
areas       <- c(200.0, 450.0, 130.0, 320.0, 500.0)
qtd_insumos <- c(1.0, 13.5, 0.65, 9.6, 2.5)

# --- área geral ---

print("=== ÁREA DE PLANTIO (m²) ===")

print("Média:")
print(mean(areas))

print("Desvio padrão:") # sd() não tá na apostila mas o enunciado pede
print(sd(areas))

print("Mínimo:")
print(min(areas))

print("Máximo:")
print(max(areas))

print("Total:")
print(sum(areas))

# --- separando por cultura ---

areas_soja  <- areas[culturas == "Soja"]
areas_milho <- areas[culturas == "Milho"]

print("=== ÁREA - SOJA (m²) ===")

print("Média:")
print(mean(areas_soja))

print("Desvio padrão:")
print(sd(areas_soja))

print("Total:")
print(sum(areas_soja))

print("=== ÁREA - MILHO (m²) ===")

print("Média:")
print(mean(areas_milho))

print("Desvio padrão:")
print(sd(areas_milho))

print("Total:")
print(sum(areas_milho))

# --- insumos geral ---

print("=== INSUMOS ===")

print("Média:")
print(mean(qtd_insumos))

print("Desvio padrão:")
print(sd(qtd_insumos))

print("Mínimo:")
print(min(qtd_insumos))

print("Máximo:")
print(max(qtd_insumos))

print("Total:")
print(sum(qtd_insumos))

# --- insumos por cultura ---

insumos_soja  <- qtd_insumos[culturas == "Soja"]
insumos_milho <- qtd_insumos[culturas == "Milho"]

print("=== INSUMOS - SOJA (L) ===")

print("Média:")
print(mean(insumos_soja))

print("Desvio padrão:")
print(sd(insumos_soja))

print("Total:")
print(sum(insumos_soja))

print("=== INSUMOS - MILHO (kg) ===")

print("Média:")
print(mean(insumos_milho))

print("Desvio padrão:")
print(sd(insumos_milho))

print("Total:")
print(sum(insumos_milho))
