# Changelog

## [1.2.4] - 2026-06-03
### Changed
- **Device ID cookie configuration:** Removed the device ID cookie days configuration in favor of a simplified setup.

## [1.2.3] - 2026-06-03
### Added
- **Logging:** Added logging of the `DEVICE_ID_COOKIE_DAYS` value for improved observability.

## [1.2.2] - 2026-06-02
### Added
- **Configurable device ID cookie:** Made the device ID cookie expiration configurable via `config.yml`.

## [1.2.1] - 2026-05-21
### Added
- **Keycloak backchannel logout:** Implemented the Keycloak backchannel logout endpoint.

## [1.2.0] - 2026-04-07
### Changed
- **Template update:** Update config files on infrastructure repository to reflect changes in the config template, ensuring consistency across environments.

## Fixed
- **Empty config handling:** Implemented logic to handle empty configuration values gracefully, preventing potential runtime errors and improving overall stability.

## [1.1.0] - 2026-03-16

### Added
- **UI Customization:** Updated the Keycloak login button template to display "Iniciar Sesion con Houndoc" and properly render the Houndoc logo instead of default Provider elements.
- **Docker Build Tuning:** Ensured static assets are copied to exactly where they are needed at Docker build context time.

## [1.0.0] - 2025-12-29

### Added
- **Initial Project Setup:** Configured the initial project with a Docker image to provide a flexible and configurable baseline environment.
