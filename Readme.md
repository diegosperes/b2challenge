# Magic numbers [![Build Status](https://travis-ci.com/diegosperes/b2challenge.svg?branch=master)](https://travis-ci.com/diegosperes/b2challenge)

Devido a natureza do problema escolhi python 3 por ser a liguagem que possuo mais familiaridade podendo usufruir de benefícios builtins sem a necessidade de depêndencias externa ou alguma implementação de controle como o caso do memoize (functools.lru_cache). Foram utilizados alguns conceitos matemáticos explicados na docstring de cada escopo afim de otimizar o artefato gerado, em caso de alguma dúvida pode entrar em contato comigo :)

## Testes

Criei um makefile para facilitar a execução dos testes: ```make tests```
Os teste foram dividídos em duas suit cases no mesmo arquivo, no entanto em um projetos mais complexo seria legar separar elas por arquivos.

## O que pode ser melhorado

No artefato gerado o loop considera um ou mais range afim de descobrir quais são os números mágicos que pertencem a esse intervalo, no entanto como podemos gerar todos os números primos maiores que 3 seria possível otimizar esse loop, também é possivel unificar intervalos como [(6, 70), (20, 85)] transformando em (6, 85) evitando interar em valores repetidos. Essas otimizações não foram feitas devido ao tempo de execução do código ser baixo ~0.3 segundos para verificar todos os números mágicos no range de 0 à 10^6 e levando em consideração que a complexidade do artefato gerado iria aumentar consideravelmente.