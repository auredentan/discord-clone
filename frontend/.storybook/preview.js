import { AppWithContext } from '../pages/_app'

export const parameters = {
	actions: { argTypesRegex: '^on[A-Z].*' },
	controls: {
		matchers: {
			color: /(background|color)$/i,
			date: /Date$/,
		},
	},
}

export const decorators = [
	(Story) => (
		<main>
			<AppWithContext>
				<Story />
			</AppWithContext>
		</main>
	),
]
