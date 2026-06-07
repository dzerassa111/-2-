import pytest
from ingredient import Ingredient  
from recipe import Recipe
from shopping_list import ShoppingList
from dietary_recipe import DietaryRecipe

class TestIngredient:
    """Тесты для класса Ingredient."""
    
    def test_ingredient_creation(self):
        """Тест создания ингредиента - проверка инициализации атрибутов."""
        ingredient = Ingredient("Мука", 500.0, "г")
        
        assert ingredient.name == "Мука"
        assert ingredient.quantity == 500.0
        assert ingredient.unit == "г"
    
    def test_ingredient_creation_with_int_quantity(self):
        """Тест создания ингредиента с целочисленным количеством."""
        ingredient = Ingredient("Яйца", 3, "шт")
        
        assert ingredient.quantity == 3.0 
        assert isinstance(ingredient.quantity, float)
    
    def test_ingredient_negative_quantity_raises_error(self):
        """Тест: при создании с отрицательным количеством выбрасывается ValueError."""
        with pytest.raises(ValueError, match="Количество должно быть положительным"):
            Ingredient("Соль", -5, "г")
    
    def test_ingredient_zero_quantity_raises_error(self):
        """Тест: при создании с нулевым количеством выбрасывается ValueError."""
        with pytest.raises(ValueError, match="Количество должно быть положительным"):
            Ingredient("Сахар", 0, "г")
    
    def test_ingredient_quantity_setter_negative_raises_error(self):
        """Тест: установка отрицательного количества через сеттер выбрасывает ValueError."""
        ingredient = Ingredient("Мука", 500, "г")
        
        with pytest.raises(ValueError, match="Количество должно быть положительным"):
            ingredient.quantity = -100
    
    def test_ingredient_quantity_setter_zero_raises_error(self):
        """Тест: установка нулевого количества через сеттер выбрасывает ValueError."""
        ingredient = Ingredient("Мука", 500, "г")
        
        with pytest.raises(ValueError, match="Количество должно быть положительным"):
            ingredient.quantity = 0
    
    def test_ingredient_quantity_setter_positive(self):
        """Тест: установка положительного количества через сеттер работает корректно."""
        ingredient = Ingredient("Мука", 500, "г")
        ingredient.quantity = 750.5
        
        assert ingredient.quantity == 750.5
    
    def test_ingredient_str_method(self):
        """Тест метода __str__ - формат '{name}: {quantity} {unit}'."""
        ingredient = Ingredient("Мука", 500.0, "г")
        
        assert str(ingredient) == "Мука: 500.0 г"
    
    def test_ingredient_str_method_with_int_quantity(self):
        """Тест метода __str__ с целочисленным количеством."""
        ingredient = Ingredient("Яйца", 3, "шт")
        
        assert str(ingredient) == "Яйца: 3.0 шт"
    
    def test_ingredient_eq_same_name_and_unit(self):
        """Тест __eq__: ингредиенты с одинаковыми name и unit равны (quantity не важно)."""
        flour1 = Ingredient("Мука", 500, "г")
        flour2 = Ingredient("Мука", 1000, "г")
        
        assert flour1 == flour2
    
    def test_ingredient_eq_different_name(self):
        """Тест __eq__: ингредиенты с разными name не равны."""
        flour = Ingredient("Мука", 500, "г")
        sugar = Ingredient("Сахар", 500, "г")
        
        assert flour != sugar
    
    def test_ingredient_eq_different_unit(self):
        """Тест __eq__: ингредиенты с разными unit не равны."""
        flour_grams = Ingredient("Мука", 500, "г")
        flour_kg = Ingredient("Мука", 0.5, "кг")
        
        assert flour_grams != flour_kg
    
    def test_ingredient_eq_same_name_same_unit(self):
        """Тест __eq__: полное совпадение (name, unit) - равны."""
        flour1 = Ingredient("Мука", 500, "г")
        flour2 = Ingredient("Мука", 500, "г")
        
        assert flour1 == flour2
    
    def test_ingredient_eq_with_non_ingredient(self):
        """Тест __eq__: сравнение с объектом другого типа возвращает False."""
        ingredient = Ingredient("Мука", 500, "г")
        
        assert ingredient != "Мука"
        assert ingredient != 500
        assert ingredient != None
    
    def test_ingredient_repr_method(self):
        """Тест метода __repr__."""
        ingredient = Ingredient("Мука", 500.0, "г")
        
        #repr должен возвращать строку, похожую на код создания объекта
        assert repr(ingredient) == "Ingredient('Мука', 500.0, 'г')"
    
    def test_ingredient_quantity_float_conversion(self):
        """Тест: количество преобразуется в float даже если передан int."""
        ingredient = Ingredient("Мука", 500, "г")
        
        assert isinstance(ingredient.quantity, float)
        assert ingredient.quantity == 500.0
        
if __name__ == "__main__":
    pytest.main([__file__, "-v"])



import pytest
from ingredient import Ingredient
from recipe import Recipe

class TestRecipe:
    
    def test_recipe_creation_with_ingredients(self):
        """Тест создания рецепта со списком ингредиентов."""
        ingredients = [
            Ingredient("Мука", 500, "г"),
            Ingredient("Яйца", 2, "шт"),
            Ingredient("Масло", 100, "г")
        ]
        recipe = Recipe("Песочное печенье", ingredients)
        
        assert recipe.title == "Песочное печенье"
        assert len(recipe.ingredients) == 3
        assert recipe.ingredients[0].name == "Мука"
        assert recipe.ingredients[1].name == "Яйца"
        assert recipe.ingredients[2].name == "Масло"
    
    def test_recipe_creation_without_ingredients(self):
        """Тест создания рецепта без ингредиентов (пустой список по умолчанию)."""
        recipe = Recipe("Пустой рецепт")
        
        assert recipe.title == "Пустой рецепт"
        assert recipe.ingredients == []
        assert len(recipe) == 0
    
    def test_recipe_creation_with_none_ingredients(self):
        """Тест создания рецепта с None вместо списка."""
        recipe = Recipe("Тестовый рецепт", None)
        
        assert recipe.title == "Тестовый рецепт"
        assert recipe.ingredients == []
    
    def test_add_ingredient_new(self):
        """Тест добавления нового ингредиента."""
        recipe = Recipe("Тестовый рецепт")
        flour = Ingredient("Мука", 500, "г")
        
        recipe.add_ingredient(flour)
        
        assert len(recipe.ingredients) == 1
        assert recipe.ingredients[0].name == "Мука"
        assert recipe.ingredients[0].quantity == 500.0
    
    def test_add_ingredient_multiple_unique(self):
        """Тест добавления нескольких разных ингредиентов."""
        recipe = Recipe("Тестовый рецепт")
        flour = Ingredient("Мука", 500, "г")
        sugar = Ingredient("Сахар", 200, "г")
        eggs = Ingredient("Яйца", 3, "шт")
        
        recipe.add_ingredient(flour)
        recipe.add_ingredient(sugar)
        recipe.add_ingredient(eggs)
        
        assert len(recipe.ingredients) == 3
    
    def test_add_ingredient_existing_sum_quantity(self):
        """Тест: при добавлении существующего ингредиента количество суммируется."""
        recipe = Recipe("Тестовый рецепт")
        flour1 = Ingredient("Мука", 500, "г")
        flour2 = Ingredient("Мука", 300, "г")
        
        recipe.add_ingredient(flour1)
        recipe.add_ingredient(flour2)
        
        assert len(recipe.ingredients) == 1
        assert recipe.ingredients[0].name == "Мука"
        assert recipe.ingredients[0].quantity == 800.0
    
    def test_add_ingredient_existing_different_unit_no_sum(self):
        """Тест: ингредиенты с одинаковым названием, но разной единицей не суммируются."""
        recipe = Recipe("Тестовый рецепт")
        flour_grams = Ingredient("Мука", 500, "г")
        flour_kg = Ingredient("Мука", 1, "кг")
        
        recipe.add_ingredient(flour_grams)
        recipe.add_ingredient(flour_kg)
        
        assert len(recipe.ingredients) == 2
        assert recipe.ingredients[0].quantity == 500.0
        assert recipe.ingredients[1].quantity == 1.0
    
    def test_add_ingredient_multiple_same_sum_quantity(self):
        """Тест: добавление одного и того же ингредиента несколько раз."""
        recipe = Recipe("Тестовый рецепт")
        flour = Ingredient("Мука", 100, "г")
        
        recipe.add_ingredient(flour)
        recipe.add_ingredient(flour)
        recipe.add_ingredient(flour)
        
        assert len(recipe.ingredients) == 1
        assert recipe.ingredients[0].quantity == 300.0
    
    def test_scale_returns_new_object(self):
        """Тест: scale возвращает новый объект Recipe, исходный не изменяется."""
        ingredients = [Ingredient("Мука", 500, "г")]
        original = Recipe("Хлеб", ingredients)
        
        scaled = original.scale(2)
        
        assert scaled is not original
        assert original.ingredients[0].quantity == 500.0
        assert len(original.ingredients) == 1
    
    def test_scale_multiplies_quantities(self):
        """Тест: scale умножает количество каждого ингредиента на коэффициент."""
        ingredients = [
            Ingredient("Мука", 500, "г"),
            Ingredient("Сахар", 200, "г"),
            Ingredient("Яйца", 3, "шт")
        ]
        recipe = Recipe("Печенье", ingredients)
        
        scaled = recipe.scale(2.5)
        
        assert scaled.ingredients[0].quantity == 1250.0  # 500 * 2.5
        assert scaled.ingredients[1].quantity == 500.0   # 200 * 2.5
        assert scaled.ingredients[2].quantity == 7.5     # 3 * 2.5
    
    def test_scale_preserves_names_and_units(self):
        """Тест: scale сохраняет названия и единицы измерения ингредиентов."""
        ingredients = [
            Ingredient("Мука", 500, "г"),
            Ingredient("Яйца", 3, "шт")
        ]
        recipe = Recipe("Печенье", ingredients)
        
        scaled = recipe.scale(2)
        
        assert scaled.ingredients[0].name == "Мука"
        assert scaled.ingredients[0].unit == "г"
        assert scaled.ingredients[1].name == "Яйца"
        assert scaled.ingredients[1].unit == "шт"
    
    def test_scale_with_ratio_one(self):
        """Тест: scale с коэффициентом 1 создаёт копию с теми же количествами."""
        ingredients = [Ingredient("Мука", 500, "г")]
        recipe = Recipe("Хлеб", ingredients)
        
        scaled = recipe.scale(1)
        
        assert scaled.ingredients[0].quantity == 500.0
        assert scaled.title == recipe.title
    
    def test_scale_with_ratio_zero_raises_error(self):
        """Тест: scale с ratio = 0 выбрасывает ValueError."""
        ingredients = [Ingredient("Мука", 500, "г")]
        recipe = Recipe("Хлеб", ingredients)
        
        with pytest.raises(ValueError, match="Коэффициент масштабирования должен быть положительным числом"):
            recipe.scale(0)
    
    def test_scale_with_ratio_negative_raises_error(self):
        """Тест: scale с отрицательным ratio выбрасывает ValueError."""
        ingredients = [Ingredient("Мука", 500, "г")]
        recipe = Recipe("Хлеб", ingredients)
        
        with pytest.raises(ValueError, match="Коэффициент масштабирования должен быть положительным числом"):
            recipe.scale(-2)
    
    def test_scale_with_ratio_float_less_than_one(self):
        """Тест: scale с коэффициентом меньше 1 (уменьшение рецепта)."""
        ingredients = [Ingredient("Мука", 500, "г")]
        recipe = Recipe("Хлеб", ingredients)
        
        scaled = recipe.scale(0.5)
        
        assert scaled.ingredients[0].quantity == 250.0
    
    def test_scale_empty_recipe(self):
        """Тест: scale для пустого рецепта."""
        recipe = Recipe("Пустой рецепт")
        
        scaled = recipe.scale(5)
        
        assert len(scaled.ingredients) == 0
        assert scaled.title == "Пустой рецепт"
    
    def test_len_empty_recipe(self):
        """Тест: __len__ возвращает 0 для пустого рецепта."""
        recipe = Recipe("Пустой рецепт")
        
        assert len(recipe) == 0
    
    def test_len_with_ingredients(self):
        """Тест: __len__ возвращает количество уникальных ингредиентов."""
        ingredients = [
            Ingredient("Мука", 500, "г"),
            Ingredient("Сахар", 200, "г"),
            Ingredient("Яйца", 3, "шт")
        ]
        recipe = Recipe("Печенье", ingredients)
        
        assert len(recipe) == 3
    
    def test_len_after_adding_ingredients(self):
        """Тест: __len__ обновляется после добавления ингредиентов."""
        recipe = Recipe("Тестовый рецепт")
        
        assert len(recipe) == 0
        
        recipe.add_ingredient(Ingredient("Мука", 500, "г"))
        assert len(recipe) == 1
        
        recipe.add_ingredient(Ingredient("Сахар", 200, "г"))
        assert len(recipe) == 2
        
        recipe.add_ingredient(Ingredient("Мука", 100, "г"))
        assert len(recipe) == 2
    
    def test_len_with_duplicate_by_name_different_unit(self):
        """Тест: ингредиенты с одинаковым названием, но разной единицей считаются разными."""
        ingredients = [
            Ingredient("Мука", 500, "г"),
            Ingredient("Мука", 1, "кг")
        ]
        recipe = Recipe("Хлеб", ingredients)
        
        assert len(recipe) == 2
    
    def test_recipe_str_method(self):
        """Тест метода __str__."""
        ingredients = [Ingredient("Мука", 500, "г")]
        recipe = Recipe("Хлеб", ingredients)
        
        str_result = str(recipe)
        assert "Хлеб" in str_result
        assert "Мука" in str_result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])




    import pytest
from ingredient import Ingredient
from recipe import Recipe
from shopping_list import ShoppingList

class TestShoppingList:
    """Тесты для класса ShoppingList."""
    
    def setup_method(self):
        """Подготовка тестовых данных перед каждым тестом."""
        self.margherita_ingredients = [
            Ingredient("Мука", 500, "г"),
            Ingredient("Сыр Моцарелла", 200, "г"),
            Ingredient("Помидоры", 300, "г"),
            Ingredient("Томатный соус", 150, "мл")
        ]
        self.margherita = Recipe("Пицца Маргарита", self.margherita_ingredients)
        
        self.four_cheese_ingredients = [
            Ingredient("Мука", 500, "г"),
            Ingredient("Сыр Пармезан", 100, "г"),
            Ingredient("Сыр Горгонзола", 100, "г"),
            Ingredient("Сыр Фета", 100, "г"),
            Ingredient("Сыр Моцарелла", 100, "г")
        ]
        self.four_cheese = Recipe("Пицца 4 Сыра", self.four_cheese_ingredients)
        
        self.salad_ingredients = [
            Ingredient("Огурцы", 200, "г"),
            Ingredient("Помидоры", 150, "г"),
            Ingredient("Сыр Фета", 100, "г"),
            Ingredient("Оливковое масло", 30, "мл")
        ]
        self.salad = Recipe("Греческий салат", self.salad_ingredients)
    
    def test_add_recipe_single(self):
        """Тест добавления одного рецепта в список покупок."""
        shopping_list = ShoppingList()
        
        shopping_list.add_recipe(self.margherita, 1)
        
        # Проверяем, что в _items добавились ингредиенты (4 штуки)
        assert len(shopping_list._items) == 4
        
        # Проверяем, что каждый элемент - кортеж (Ingredient, recipe_title)
        for ingredient, recipe_title in shopping_list._items:
            assert isinstance(ingredient, Ingredient)
            assert recipe_title == "Пицца Маргарита"
    
    def test_add_recipe_with_portions(self):
        """Тест добавления рецепта с масштабированием на количество порций."""
        shopping_list = ShoppingList()
        
        shopping_list.add_recipe(self.margherita, 2)
        
        # Проверяем, что количество каждого ингредиента удвоено
        quantities = {item[0].name: item[0].quantity for item in shopping_list._items}
        assert quantities["Мука"] == 1000.0  # 500 * 2
        assert quantities["Сыр Моцарелла"] == 400.0  # 200 * 2
        assert quantities["Помидоры"] == 600.0  # 300 * 2
        assert quantities["Томатный соус"] == 300.0  # 150 * 2
    
    def test_add_recipe_multiple_recipes(self):
        """Тест добавления нескольких рецептов в список покупок."""
        shopping_list = ShoppingList()
        
        shopping_list.add_recipe(self.margherita, 1)
        shopping_list.add_recipe(self.four_cheese, 1)
        
        # Всего ингредиентов: 4 + 5 = 9 (без учёта дубликатов в _items)
        assert len(shopping_list._items) == 9
    
    def test_add_recipe_zero_portions_raises_error(self):
        """Тест: добавление с portions = 0 выбрасывает ValueError."""
        shopping_list = ShoppingList()
        
        with pytest.raises(ValueError, match="Количество порций должно быть положительным"):
            shopping_list.add_recipe(self.margherita, 0)
    
    def test_add_recipe_negative_portions_raises_error(self):
        """Тест: добавление с отрицательными portions выбрасывает ValueError."""
        shopping_list = ShoppingList()
        
        with pytest.raises(ValueError, match="Количество порций должно быть положительным"):
            shopping_list.add_recipe(self.margherita, -1)
    
    def test_add_recipe_float_portions(self):
        """Тест: добавление с дробным количеством порций."""
        shopping_list = ShoppingList()
        
        shopping_list.add_recipe(self.margherita, 1.5)
        
        quantities = {item[0].name: item[0].quantity for item in shopping_list._items}
        assert quantities["Мука"] == 750.0
        assert quantities["Сыр Моцарелла"] == 300.0
    
    def test_remove_recipe_existing(self):
        """Тест удаления существующего рецепта."""
        shopping_list = ShoppingList()
        shopping_list.add_recipe(self.margherita, 1)
        shopping_list.add_recipe(self.four_cheese, 1)
        
        assert len(shopping_list._items) == 9
        
        shopping_list.remove_recipe("Пицца Маргарита")
        
        assert len(shopping_list._items) == 5
        for _, recipe_title in shopping_list._items:
            assert recipe_title == "Пицца 4 Сыра"
    
    def test_remove_recipe_removes_all_occurrences(self):
        """Тест: удаление рецепта удаляет все его ингредиенты (даже если добавлен несколько раз)."""
        shopping_list = ShoppingList()
        shopping_list.add_recipe(self.margherita, 1)
        shopping_list.add_recipe(self.margherita, 2)  # добавили ещё раз
        
        assert len(shopping_list._items) == 8 
        
        shopping_list.remove_recipe("Пицца Маргарита")
        
        assert len(shopping_list._items) == 0
    
    def test_remove_recipe_non_existent(self):
        """Тест: удаление несуществующего рецепта не вызывает ошибку."""
        shopping_list = ShoppingList()
        shopping_list.add_recipe(self.margherita, 1)
        
        shopping_list.remove_recipe("Несуществующая пицца")
        
        # Список не изменился
        assert len(shopping_list._items) == 4
    
    def test_remove_recipe_from_empty_list(self):
        """Тест: удаление рецепта из пустого списка не вызывает ошибку."""
        shopping_list = ShoppingList()
        
        shopping_list.remove_recipe("Любой рецепт")
        
        assert len(shopping_list._items) == 0
    
    def test_remove_recipe_partial_match(self):
        """Тест: удаление по точному совпадению названия (не частичному)."""
        shopping_list = ShoppingList()
        shopping_list.add_recipe(self.margherita, 1)
        shopping_list.add_recipe(self.four_cheese, 1)
        
        shopping_list.remove_recipe("Пицца")  # не точное совпадение
        
        # Ничего не удалилось
        assert len(shopping_list._items) == 9
    
    def test_get_list_single_recipe(self):
        """Тест: get_list для одного рецепта возвращает ингредиенты без изменений."""
        shopping_list = ShoppingList()
        shopping_list.add_recipe(self.margherita, 1)
        
        result = shopping_list.get_list()
        
        assert len(result) == 4
        # Проверяем, что все ингредиенты на месте
        ingredients_dict = {ing.name: ing.quantity for ing in result}
        assert ingredients_dict["Мука"] == 500.0
        assert ingredients_dict["Сыр Моцарелла"] == 200.0
        assert ingredients_dict["Помидоры"] == 300.0
        assert ingredients_dict["Томатный соус"] == 150.0
    
    def test_get_list_sums_same_ingredients(self):
        """Тест: одинаковые ингредиенты из разных рецептов суммируются."""
        shopping_list = ShoppingList()
        shopping_list.add_recipe(self.margherita, 1)  # Мука: 500г
        shopping_list.add_recipe(self.four_cheese, 1)  # Мука: 500г
        
        result = shopping_list.get_list()
        
        # Находим муку в результате
        flour = next(ing for ing in result if ing.name == "Мука")
        assert flour.quantity == 1000.0  # 500 + 500
    
    def test_get_list_sums_multiple_occurrences(self):
        """Тест: суммирование ингредиентов, встречающихся в нескольких рецептах."""
        shopping_list = ShoppingList()
        shopping_list.add_recipe(self.margherita, 1)   # Сыр Моцарелла: 200г
        shopping_list.add_recipe(self.four_cheese, 1)  # Сыр Моцарелла: 100г
        
        result = shopping_list.get_list()
        
        mozzarella = next(ing for ing in result if ing.name == "Сыр Моцарелла")
        assert mozzarella.quantity == 300.0
    
    def test_get_list_no_duplicates(self):
        """Тест: get_list не содержит дубликатов ингредиентов."""
        shopping_list = ShoppingList()
        shopping_list.add_recipe(self.margherita, 1)
        shopping_list.add_recipe(self.four_cheese, 1)
        shopping_list.add_recipe(self.salad, 1)
        
        result = shipping_list.get_list()
        
        # Проверяем, что нет двух ингредиентов с одинаковыми name и unit
        seen = set()
        for ing in result:
            key = (ing.name, ing.unit)
            assert key not in seen
            seen.add(key)
    
    def test_get_list_sorted_by_name(self):
        """Тест: get_list возвращает список, отсортированный по названию ингредиента."""
        shopping_list = ShoppingList()
        shopping_list.add_recipe(self.four_cheese, 1)
        
        result = shopping_list.get_list()
        
        # Ожидаемый порядок по алфавиту
        names = [ing.name for ing in result]
        assert names == sorted(names)
    
    def test_get_list_sorted_with_multiple_recipes(self):
        """Тест: сортировка с несколькими рецептами."""
        shopping_list = ShoppingList()
        shopping_list.add_recipe(self.margherita, 1)
        shopping_list.add_recipe(self.four_cheese, 1)
        shopping_list.add_recipe(self.salad, 1)
        
        result = shopping_list.get_list()
        
        names = [ing.name for ing in result]
        assert names == sorted(names)
    
    def test_get_list_empty(self):
        """Тест: get_list для пустого списка возвращает пустой список."""
        shopping_list = ShoppingList()
        
        result = shopping_list.get_list()
        
        assert result == []
    
    def test_get_list_preserves_units(self):
        """Тест: get_list правильно различает ингредиенты по единицам измерения."""
        shopping_list = ShoppingList()
        # Добавляем муку в граммах и килограммах
        recipe1 = Recipe("Рецепт 1", [Ingredient("Мука", 500, "г")])
        recipe2 = Recipe("Рецепт 2", [Ingredient("Мука", 1, "кг")])
        
        shopping_list.add_recipe(recipe1, 1)
        shopping_list.add_recipe(recipe2, 1)
        
        result = shopping_list.get_list()
        
        # Должно быть два разных ингредиента
        assert len(result) == 2
        flour_grams = next(ing for ing in result if ing.unit == "г")
        flour_kg = next(ing for ing in result if ing.unit == "кг")
        assert flour_grams.quantity == 500.0
        assert flour_kg.quantity == 1.0
    
    def test_add_two_shopping_lists(self):
        """Тест: объединение двух списков покупок."""
        list1 = ShoppingList()
        list2 = ShoppingList()
        
        list1.add_recipe(self.margherita, 1)
        list2.add_recipe(self.four_cheese, 1)
        
        combined = list1 + list2
        
        assert len(combined._items) == 9
    
    def test_add_does_not_modify_original_lists(self):
        """Тест: исходные списки не изменяются при объединении."""
        list1 = ShoppingList()
        list2 = ShoppingList()
        
        list1.add_recipe(self.margherita, 1)
        list2.add_recipe(self.four_cheese, 1)
        
        original_len1 = len(list1._items)
        original_len2 = len(list2._items)
        
        combined = list1 + list2
        
        assert len(list1._items) == original_len1
        assert len(list2._items) == original_len2
    
    def test_add_returns_new_object(self):
        """Тест: __add__ возвращает новый объект ShoppingList."""
        list1 = ShoppingList()
        list2 = ShoppingList()
        
        list1.add_recipe(self.margherita, 1)
        list2.add_recipe(self.four_cheese, 1)
        
        combined = list1 + list2
        
        assert combined is not list1
        assert combined is not list2
    
    def test_add_with_empty_list(self):
        """Тест: объединение с пустым списком."""
        list1 = ShoppingList()
        list2 = ShoppingList()
        
        list1.add_recipe(self.margherita, 1)
        
        combined = list1 + list2
        
        assert len(combined._items) == len(list1._items)
        assert combined._items == list1._items
    
    def test_add_with_same_recipe_in_both_lists(self):
        """Тест: объединение списков с одинаковыми рецептами."""
        list1 = ShoppingList()
        list2 = ShoppingList()
        
        list1.add_recipe(self.margherita, 1)
        list2.add_recipe(self.margherita, 2)
        
        combined = list1 + list2
        
        # Должно быть 4 + 4 = 8 элементов (дубликаты не суммируются на уровне _items)
        assert len(combined._items) == 8
    
    def test_add_preserves_recipe_titles(self):
        """Тест: при объединении сохраняется привязка к рецептам."""
        list1 = ShoppingList()
        list2 = ShoppingList()
        
        list1.add_recipe(self.margherita, 1)
        list2.add_recipe(self.four_cheese, 1)
        
        combined = list1 + list2
        
        titles = {recipe_title for _, recipe_title in combined._items}
        assert "Пицца Маргарита" in titles
        assert "Пицца 4 Сыра" in titles


if __name__ == "__main__":
    pytest.main([__file__, "-v"])



