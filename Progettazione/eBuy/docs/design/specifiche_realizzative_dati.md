# Specifica realizzativa dei tipi di dato

## IntGEZ:
  - Eredita da int
  - Impedisce inserimento valori < 0

## IntGZ:
  - Eredita da IntGEZ
  - Impedisce inserimento valori <= 0

## RealGEZ:
  - Eredita da float
  - Impedisce inserimento valori < 0

## RealGZ:
  - Eredita da RealGEZ
  - Impedisce inserimento valori <= 0

## StatoPost:
  - Eredita da StrEnum
  - implementa le varianti: nuovo e usato

## Condizione:
  - Enumerazione da StrEnum:
  - implementa le varianti: ottimo, buono, discreto, da sistemare
  
## TimeDelta_GZ
  - Eredita da timedelta
  - Impedisce valori <= 0

## Tipologia:
  - Eredita da StrEnum
  - due istanze possibili: nuovo, usato
  
## URL:
  - regex d'esempio 
