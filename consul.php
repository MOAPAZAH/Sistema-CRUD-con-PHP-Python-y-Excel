<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Recibir datos del formulario
    $nombre = $_POST['nombre'];
    $edad = $_POST['edad'];
    $accion = $_POST['accion'];

    // Comando a ejecutar en Python, pasando los parámetros
    $command = escapeshellcmd("python consulta.py $nombre $edad $accion");
    $output = shell_exec($command);
    echo "<pre>" . htmlspecialchars($output) . "</pre>";
    // echo $nombre;
    // echo $edad;
    // echo $accion;
    // // Mostrar el resultado del script Python
    // echo $output;
}
?>
