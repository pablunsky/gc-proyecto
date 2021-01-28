<h1>
Clasificación de genomas completos de Arbovirus: Dengue, Zika y Chikungunya empleando CGR y Regresión Logística
</h1>

Javier de León, Pablo Hernandez, Luis Pablo Kuri



<h2> Resumen
</h2>
<p>Utilizando el punto medio y la métrica euclidiana se realizó la representación del CGR de al menos 50 muestras del genoma completo de los virus, no se realizaron distinciones entre las cepas virales ni serotipos en el caso de Dengue. Luego se utilizó un modelo de regresión logística que realizó comparaciones a pares entre los genomas. Esta herramienta de clasificación fue montada sobre una página web a la cual es posible acceder para verificar la procedencia de un genoma del que se desconozca su clasificación mediante un archivo fasta. Debido al tamaño de nuestro dataset no se debe descartar la posibilidad de haber realizado overfitting, aun así las pruebas realizadas han dado resultados satisfactorios. Para futuro es posible realizar un modelo más robusto aumentando la cantidad de muestras y realizando técnicas de bootstrapping.

</p>

<h2> Objetivo
</h2>
<p> Clasificar las enfermedades de Dengue, Zika y chikungunya haciendo uso de regresiones logísticas entrenadas a pares con imágenes generadas por CGR
</p>

<h2> Justificación
</h2>
Las enfermedades causadas por arbovirus poseen prevalencia zonas tropicales y subtropicales como México y Guatemala. Estos suelen presentarse en forma epidémica y son similares en su expresión clínica, pudiendo desarrollarse desde enfermedades asintomáticas hasta graves con consecuencias como síndromes neuronales (Guillain-Barré) o muerte. La vía de transmisión del virus es por picadura de mosquitos infectados del género Aedes.

<h2> Hipótesis
</h2>
<p> Utilizar modelos de regresiones logísticas entrenados a pares, es posible realizar una distinción de las imágenes de las firmas genéticas de los virus estudiados al utilizar una representación del juego de caos específica.

</p>
<h2> Diagrama Metodológico
</h2>

| ![space-1.jpg](https://github.com/pablunsky/gc-proyecto/blob/master/New%20folder%20(6)/diagrama.png) | 
|:--:| 



 <br />


<h2> Resultados
</h2>
 <br />
<h3> Chinkungunya
</h3>
 <br />

| ![space-1.jpg](https://github.com/pablunsky/gc-proyecto/blob/master/New%20folder%20(6)/CHIKUNGUNYA-nuccoreEU372006.1.fasta.jpg) | 
|:--:| 
| *Mapa de Calor de la CGR de Chinkungunya* |
    
| ![space-1.jpg](https://github.com/pablunsky/gc-proyecto/blob/master/New%20folder%20(6)/REGRESION%20CHIKUNGUNYA.png) | 
|:--:| 
| *Resultado del Modelo para Chinkungunya* |
| ![space-1.jpg](https://github.com/pablunsky/gc-proyecto/blob/master/New%20folder%20(6)/SCATTER%20CHIKUNGUNYA.png) | 
|*Scatter Chinkungunya*| 



 
<h3> Dengue
</h3>
 <br />

| ![space-1.jpg](https://github.com/pablunsky/gc-proyecto/blob/master/New%20folder%20(6)/DENGUE-nuccoreAF309641.1.fasta.jpg) | 
|:--:| 
| *Mapa de Calor de la CGR del Dengue* |

     
     
| ![space-1.jpg](https://github.com/pablunsky/gc-proyecto/blob/master/New%20folder%20(6)/REGRESION%20DENGUE.png) | 
|:--:| 
| *Resultado del Modelo para Dengue* |
<br />
 
| ![space-1.jpg](https://github.com/pablunsky/gc-proyecto/blob/master/New%20folder%20(6)/SCATTER%20DENGUE.png) | 
|:--:| 
| *Scatter Dengue* |

<h3> Zika
</h3>
 <br />

| ![space-1.jpg](https://github.com/pablunsky/gc-proyecto/blob/master/New%20folder%20(6)/DENGUE-nuccoreAF309641.1.fasta.jpg) | 
|:--:| 
| *Mapa de Calor de la CGR de Zika* |
     
| ![space-1.jpg](https://github.com/pablunsky/gc-proyecto/blob/master/New%20folder%20(6)/REGRESION%20ZIKA.png) | 
|:--:| 
| *Resultado del Modelo para Zika* |

<br />

| ![space-1.jpg](https://github.com/pablunsky/gc-proyecto/blob/master/New%20folder%20(6)/SCATTER%20ZIKA.png) | 
|:--:| 
| *Scatter Zika* |


<h2> Conclusión
</h2>


<p> Las firmas genéticas de los virus utilizados pueden emplearse para la creación de un modelo de CGR y regresión logística el cual permite la clasificación de los virus.

</p>


<h2> Referencias
 https://www.youtube.com/watch?v=3m5MGvCX3nI&list=PLE0_iBOs1R0kf4_6D_UyMPFZvgDEKj0rH&index=30
 <br />
 http://epidemiologia.mspas.gob.gt/files/Publicaciones%202018/Protocolos/Vigilancia%20Epidemiol%C3%B3gica%20Integrada%20de%20Arbovirosis.pdf
 <br />
 https://www.ncbi.nlm.nih.gov/nuccore/?term=Chikungunya+virus+complete+genome
 <br />
 https://www.ncbi.nlm.nih.gov/nuccore/?term=zika+complete+genome
 <br />
 https://www.ncbi.nlm.nih.gov/nuccore/?term=dengue+virus+complete+genome
</h2>











