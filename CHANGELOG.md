# Changelog

## [2.0.0] â€” QA release branch

### Added
- Auth module (`src/auth/login.py`)
- REST API endpoints (`src/api/endpoints.py`)
- Cache layer with TTL (`src/cache/cache_fix.py`)
- Security utilities (`src/security/patch.py`)

### Fixed
- Session invalidation on logout
- Cache expiry edge case

### Changed
- Version bumped to 2.0.0
