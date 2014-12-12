Laravel
===

A simple blog application developed with PHP/[Laravel](http://laravel.com)

## Requirement

* Apache Web Server
* PHP 5.3.2 or above
* Laravel 4
* MySQL

## Plugin
* cartalyst/sentry
* edvinaskrucas/notification
* fzaninotto/faker
* way/generators

## Installation

1. Create Database, make sure to update the database configuration  `app/config/database.php` same with your MySQL configuration
2. Create Sentry Tables for auth system, run the command `php artisan migrate --package=cartalyst/sentry`
3. Create application tables, run the command `php artisan migrate:make create_article_table --create=articles` to generate migration file, which you could add fields of the table, for creating table with the command `php artisan migrate`.
4. Create model, which you could manage the model fields.Run the command `php artisan generate:model article`
5. Generate fake data for testing. I suggest you to use the plugins `Faker\Factory` and `way/generators`. Run the command `php artisan generate:seed article` to generate seed file, and update the seed file like below:
	
	`Article::create([   
	     'title'   => $faker->sentence($nbWords = 5),  
	     'slug'    => 'first-post',   
	     'body'    => $faker->paragraph($nbSentences = 5),   
	     'user_id' => 1,
	]);`

update DatabaseSeeder.php to register seed file with the code `$this->call('ArticleTableSeeder');`
6. Here to run: `php artisan serve --port=8080`.


