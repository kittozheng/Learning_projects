<?php

namespace App\Controllers\Admin;

use Auth, BaseController, Form, Input, Redirect, Sentry, View;

class AuthController extends BaseController {

	/**
	 *
	 * Show login page
	 * @return Response
	 */
	public function getLogin()
	{
		return View::make('admin.auth.login');
	}

	/**
	 * Post Login Auth
	 *
	 * @return Redirect
	 */
	public function postLogin()
	{
		$credentials = array(
			'email'		=>	Input::get('email'),
			'password'	=> 	Input::get('password')
		);

		try{
			$user = Sentry::authenticate($credentials, false);

			if($user){
				return Redirect::route('admin.pages.index');
			}
		}catch(\Exception $e){
			return Redirect::route('<admin class="lo"></admin>gin')->withErrors(array('login' => $e->getMessage()));
		}
	}

	/**
	 * Logout
	 *
	 * @return Redirect
	 */
	public function getLogout()
	{
		Sentry::logout();

		return Redirect::route('admin.login');
	}

}