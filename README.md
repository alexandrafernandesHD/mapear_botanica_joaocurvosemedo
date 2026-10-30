# Repositório - Mapear a botânica médica dos séculos XVII e XVIII: o caso de João Curvo Semedo 

<h1>Descrição</h2>
<p>Neste repositório estão disponíveis os códigos de linguagem Python utilizados no decorrer da dissertação, assim como as transcrições que resultaram do trabalho desenvolvido, a sua anotação em linguagem XML e o esquema DTD da anotação.</p>
<p>As tabelas Excel que permitem que o utilizador as organize por filtros foram incluídas neste repositório.</p>
<p>Fornecemos ainda os resultados das extrações sem qualquer edição.</p>

<h2>Pastas que compõem o Repositório</h2>
<p><strong>Anotação</strong></p>
<p><strong>Códigos</strong></p>
<p><strong>Outputs</strong></p>
<p><strong>Tabelas</strong></p>
<p><strong>Transcrições</strong></p>

<h2>Conteúdo das Pastas</h2>

<p><strong>Anotação</strong></p>
<p>Nesta pasta é possível consultar o esquema DTD utilizado para anotar o <i>Memorial</i> e a versão anotada do mesmo com recurso à linguagem XML.</p>

**Documentos**
* memorialsimplex.dtd - Esquema DTD que nos permitiu anotar o <i>Memorial de Varios Simplices</i> de acordo com a hierarquia e as declarações estabelecidas. 
* memorialanotado.xml - Ficheiro XML válido com o <i>Memorial de Varios Simplices</i> anotado segundo o esquema DTD anterior. 
 ---------- 
<p><strong>Códigos</strong></p>
<p>Nesta pasta é possível consultar os códigos Python utilizados.</p> 
<p>Estes incluem o código que permitiu a normalização do "s" longo e os códigos utilizados para extrair segmentos e contar etiquetas.</p>

**Documentos**
* normalizar.py - Código para normalizar o "s" longo.
* contagemetiquetas.pt - Código para contar o número total de ocorrências de uma etiqueta específica no documento anotado.
* contagempordiv.py - Código para contar o número total de ocorrências de uma etiqueta específica por entrada de símplice.
* extrairconteudo.py - Código utilizado para extrair informação do Memorial por etiqueta. 
 ---------- 
<p><strong>Outputs</strong></p>

<p>Nesta pasta é possível consultar os resultados de extrações realizadas através do código "extrairconteudo.py".</p>
<p>Estes consistem em documentos txt sem qualquer edição.</p>
<p>Os gráficos e as tabelas da dissertação foram elaborados através da informação destes documentos.</p>

**Documentos**
* conditions.txt - Extração da etiqueta <condition> e seu conteúdo.
* simples.txt - Extração da etiqueta <simples> e seu conteúdo.
* person.txt - Extração da etiqueta <person> e seu conteúdo.
* origin.txt - Extração da etiqueta <origin> e seu conteúdo.
* bibl.txt - Extração da etiqueta <bibl> e seu conteúdo.
---------- 
<p><strong>Tabelas</strong></p>
<p>Nesta pasta é possível consultar as tabelas construídas no âmbito da presente dissertação.</p>
<p>Estas tabelas permitem selecionar parâmetros e organizar/filtrar os dados de acordo com diferentes critérios, dependendo da tabela.</p>
<p>Para esse fim, basta clicar na seta de filtro presente no cabeçalho da tabela.</p>

**Documentos**
* botanica_joaocurvosemedo.xlsx - Livro de Excel que contém as seguintes folhas:
<p>Bibliografia - Tabela com a bibliografia extraída no Memorial, os seus autores e número de ocorrências.</p>
<p>Condições - Tabela com a lista de condições anotadas e o seu número de ocorrências.</p>
<p>Tipo-Condições - Tabela com a lista de condições, seus tipos e número de ocorrências.</p> 
<p>Origem - Tabela com os símplices por origem declarada no <i>Memorial</i>.</p>
<p>Pessoas - Tabela com as pessoas mencionadas e número de ocorrências.</p>

---------- 
<p><strong>Transcrição</strong></p>
<p>Nesta pasta encontram-se as duas versões resultantes do processo de transcrição do <i>Memorial</i>.</p>
<p>São documentos <i>plain text</i> de extensão .txt.</p>

**Documentos**
* memorial.txt - Transcrição do <i>Memorial</i> com a ortografia tal como na obra original.
* memorial_s.txt - Transcrição do <i>Memorial</i> onde o "s" longo foi normalizado para "s".
---------- 
Documentos elaborados por Susana Alexandra Coutinho de Oliveira e Marques Fernandes 
Mestrado em Humanidades Digitais
Escola de Letras, Artes e Ciências Humanas (ELACH), Universidade do Minho
Outubro de 2026
