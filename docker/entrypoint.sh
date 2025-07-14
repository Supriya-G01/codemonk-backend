#!/usr/bin/env bash
set -e

# Wait for Postgres
echo "⏳ Waiting for postgres..."
until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 1
done
echo "✅ Postgres is up"

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec "$@"
