{ pkgs }:

pkgs.mkShell {
  packages = with pkgs; [
    python3
    postgresql
    postgresql.pg_config
    openldap
    cyrus_sasl
  ];

  LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc.lib
  ];

  shellHook = ''
    export DEVENV_NAME="root"
  '';
}
