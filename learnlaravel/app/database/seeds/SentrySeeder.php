<?php

class SentrySeeder extends Seeder{

	 public function run(){
	 	DB::table('users')->delete();
	 	DB::table('groups')->delete();
	 	DB::table('users_groups')->delete();

	 	Sentry::getUserProvider()->create(array(
	 		'email'		=> 	'kittozhengszu@gmail.com',
	 		'password'	=>	'123',
	 		'first_name'	=> 	'Kitto',
	 		'last_name'	=> 	'Zheng',
	 		'activated'	=>	1,
	 	));

	 	Sentry::getGroupProvider()->create(array(
	 		'name'		=>	'Admin',
	 		'permissions'	=>	['admin'=>1],
	 	));

	 	// Add user to grooup
	 	$adminUser =  Sentry::getUserProvider()->findByLogin('kittozhengszu@gmail.com');
	 	$adminGroup =  Sentry::getGroupProvider()->findByName('Admin');
	 	$adminUser->addGroup($adminGroup);
	 }
}

?>