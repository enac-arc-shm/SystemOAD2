Introducción

Este documento define los permisos detallados para cada rol establecido en el servidor Linux. También se describe cómo se lleva a cabo la auditoría de acceso para garantizar la seguridad y trazabilidad de las acciones realizadas por los usuarios.

Roles Definidos

Root: Acceso total al sistema.

Administrador: Acceso limitado al grupo docker y configuración/administración de servicios de red.

Empleado: Permisos exclusivamente de lectura.

Permisos por Rol

Root (Superusuario)

Permisos:

Administración completa del sistema (usuarios, grupos, servicios, etc.).

Acceso y modificación a todos los directorios y archivos.

Instalación y configuración de software.

Gestión de todos los servicios y recursos del sistema.

Auditoría completa (lectura de logs y generación de reportes).

Justificación:

Este rol está reservado únicamente para tareas críticas del sistema.

Acceso:

Solo puede ser utilizado mediante su o acceso directo al usuario root.
