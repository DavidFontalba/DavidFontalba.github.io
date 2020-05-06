<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
<head>
<style>
table {
 border: 1px solid red;
}
tr {
 background-color: #FFFFFF;
 text-align: center;
}
</style>
</head>
<body>
 <h2>El Tiempo en Córdoba</h2>
 <table>
 <tr >
 <th>Fecha</th>
  <th>Estado del cielo</th>
   <th>T. Mínima</th>
    <th>T. Máxima</th>
 </tr>
 <xsl:for-each select="root/prediccion/dia">
 <tr>
 <td><xsl:value-of select="@fecha"/></td>
  <td><xsl:value-of select="estado_cielo/@descripcion"/></td>
   <td><xsl:value-of select="temperatura/minima"/></td>
    <td><xsl:value-of select="temperatura/maxima"/></td>
 </tr>
 </xsl:for-each>
 </table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>