# CRON.md - Portainer Agent Scheduled Tasks

## Scheduled Tasks

### Environment Snapshot (Every 15 minutes)
- Take snapshots of all environments to keep dashboard data fresh
- Use `snapshot_all_endpoints` tool

### Stack Health Check (Every 30 minutes)
- List all stacks and check their status
- Report any stacks in error state
- Check for stacks that have been stopped unexpectedly

### User Audit (Daily)
- List all users and check for inactive accounts
- Review API token expiration dates
- Report any security concerns
