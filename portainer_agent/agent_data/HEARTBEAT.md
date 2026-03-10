# HEARTBEAT.md - Portainer Agent Health Checks

## Health Check

### Portainer Connectivity
- Verify connection to the Portainer instance using `get_status`
- Confirm authentication by calling `get_current_user`

### Environment Health
- List all environments with `get_endpoints`
- Check for environments that are offline or have stale snapshots
- Report any environments with connectivity issues

### Stack Status
- List all stacks with `get_stacks`
- Identify any stacks in error state or that failed to deploy
- Report stacks that may need attention

### System Status
- Get system info with `get_system_info`
- Check system version for available updates
- Monitor system resource usage
