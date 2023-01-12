# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Changed

- Updated `~.Formatter` docstring to better explain the addition of custom methods.
- Updated `~.Formatter.__missing__` to format additional exceptions as `ERROR: <excname>: <exctext>`
  instead of `ERROR: <exctext>`.
- Updated `~.Formatter.__missing__` to return info embed separately from additional items.
- Updated `~.ErrorHandler.error` to conform to the above.
- Updated `~.ErrorHandler.error` to set title of embed (or message content if a file) of each value
  in the additional information list returned by `~.Formatter.__missing__` to
  `"Additional information <x> of <y>"` before sending.

## [0.0.2] - 2023-01-12

### Added

- Added this changelog.
- Added class docstring to `~.ErrorHandler`.
- Added class docstring to `~.Formatter`.

### Changed

- Updated the `~.ErrorHandler` class to handle custom exception methods in `~.Formatter`, formatted
  as `def custom_<exc_name>(self, exc: Exception) -> str`.
- Fixed docstring in `~.ErrorHandler.__init__` to properly elaborate all arguments.
