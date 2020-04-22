﻿<?xml version="1.0" encoding="UTF-8"?>
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
 <h2>My CD Collection</h2>
 <table>
 <tr >
 <th>Title</th>
 <th>Artist</th>
  <th>Price</th>
  <th>Year</th>
 </tr>
 <xsl:for-each select="//cd"> 

 <tr>
 <td><xsl:value-of select="title"/></td>
 <td><xsl:value-of select="artist"/></td>
 <xsl:choose>
 <xsl:when test="price &lt; 10">
 <td style="background-color:green">
<xsl:value-of select="price" ></xsl:value-of>
 </td>
 </xsl:when>
  <xsl:when test="price &lt; 20">
 <td style="background-color:yellow">
<xsl:value-of select="price" ></xsl:value-of>
 </td>
 </xsl:when>
  <xsl:when test="price &lt; 30">
 <td style="background-color:red">
<xsl:value-of select="price" ></xsl:value-of>
 </td>
 </xsl:when>
  <xsl:when test="price > 30">
 <td style="background-color:pink">
<xsl:value-of select="price" ></xsl:value-of>
 </td>
 </xsl:when>
 
 </xsl:choose>
  <td><xsl:value-of select="year"/></td>
 </tr>
 </xsl:for-each>
 </table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>