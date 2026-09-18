#!/bin/sh
set -eu
LOCK="${1:-fpga/qualification/minimig-aga.lock}"
# shellcheck disable=SC1090
. "$LOCK"
DEST="${2:-build/upstream/minimig-aga}"
rm -rf "$DEST"
mkdir -p "$(dirname "$DEST")"
git init "$DEST"
git -C "$DEST" remote add origin "$UPSTREAM_REPOSITORY"
git -C "$DEST" fetch --depth 1 origin "$UPSTREAM_COMMIT"
git -C "$DEST" checkout --detach FETCH_HEAD
test "$(git -C "$DEST" rev-parse HEAD)" = "$UPSTREAM_COMMIT"
git -C "$DEST" rev-parse HEAD > "$DEST/RETROSBC_PINNED_REVISION"
