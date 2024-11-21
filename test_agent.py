from poke_env import AccountConfiguration

# No authentication required
my_account_config = AccountConfiguration("my_username", None)
player = Player(account_configuration=my_account_config)

# Authentication required
my_account_config = AccountConfiguration("my_username", "super-secret-password")
player = Player(account_configuration=my_account_config, server_configuration=...)

# Auto-generated configuration for local use
player = Player()