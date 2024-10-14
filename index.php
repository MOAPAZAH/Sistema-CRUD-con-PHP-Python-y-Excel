<!DOCTYPE html>
<html>
<head>
    <title>Formulario de CRUD</title>
</head>
<body>

<h2>Gestión de Registros</h2>

<!-- Formulario para añadir, modificar, eliminar, buscar -->
<form action="consul.php" method="POST">
    <label for="nombre">Nombre:</label><br>
    <input type="text" id="nombre" name="nombre"><br><br>

    <label for="edad">Edad:</label><br>
    <input type="text" id="edad" name="edad"><br><br>

    <label for="accion">Selecciona una acción:</label><br>
    <select name="accion">
        <option value="buscar">Buscar</option>
        <option value="modificar">Modificar</option>
        <option value="eliminar">Eliminar</option>
        <option value="añadir">Añadir</option>
    </select><br><br>

    <input type="submit" value="Ejecutar">
</form>

</body>
</html>
