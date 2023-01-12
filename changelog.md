# Changelog

All notable changes to this project will be documented in this file.

## [0.0.2] - 2023-01-12

### Added

- Added this changelog.
- Added class docstring to `~.ErrorHandler`.
- Added class docstring to `~.Formatter`.

### Changed

- Updated the `~.ErrorHandler` class to handle custom exception methods in `~.Formatter`, formatted
  as `def custom_<exc_name>(self, exc: Exception) -> str`.
- Fixed docstring in `~.ErrorHandler.__init__` to properly elaborate all arguments.
