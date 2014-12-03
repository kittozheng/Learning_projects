@if (Sentry::check())
	<ul>
		<li class="{{ Request::is('admin/pages*') ? 'active' : null }}">
			<a href="{{ URL::route('admin.pages.index') }}">
				<i class="icon-book"> Pages</i>
			</a>
		</li>
		<li class="{{ Request::is('admin/articles*') ? 'active' : null}}">
			<a href="{{ URL::route('admin.articles.index') }}">
				<i class="icon-edit"> Artilce</i>
			</a>
		</li>	
		<li><a href="{{ URL::route('admin.logout') }}"><i class="icon-lock"></i> Logout </a></li>
	</ul>	
@endif