-- CreateTable
CREATE TABLE "armors" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "culture" TEXT NOT NULL,
    "weight" DOUBLE PRECISION NOT NULL,
    "type" TEXT NOT NULL,
    "head_armor" INTEGER NOT NULL,
    "body_armor" INTEGER NOT NULL,
    "arm_armor" INTEGER NOT NULL,
    "leg_armor" INTEGER NOT NULL,

    CONSTRAINT "armors_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "bows" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "culture" TEXT NOT NULL,
    "weight" DOUBLE PRECISION NOT NULL,
    "type" TEXT NOT NULL,
    "subtype" TEXT NOT NULL,
    "difficulty" INTEGER NOT NULL,
    "speed_rating" INTEGER NOT NULL,
    "missile_speed" INTEGER NOT NULL,
    "accuracy" INTEGER NOT NULL,
    "damage" INTEGER NOT NULL,
    "fire_on_mount" BOOLEAN NOT NULL,
    "reload_on_mount" BOOLEAN NOT NULL,

    CONSTRAINT "bows_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "castles" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "owner_id" TEXT NOT NULL,
    "owner_name" TEXT NOT NULL,
    "culture" TEXT NOT NULL,
    "x_position" DOUBLE PRECISION NOT NULL,
    "y_position" DOUBLE PRECISION NOT NULL,
    "prosperity" INTEGER NOT NULL,
    "wall_level" INTEGER NOT NULL,
    "bound_village_1" TEXT,
    "bound_village_2" TEXT,

    CONSTRAINT "castles_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "clans" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "owner" TEXT NOT NULL,
    "kingdom" TEXT NOT NULL,
    "culture" TEXT NOT NULL,
    "tire" INTEGER NOT NULL,
    "is_ruling_clan" BOOLEAN NOT NULL,

    CONSTRAINT "clans_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "cultures" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "is_main_culture" BOOLEAN NOT NULL,
    "desc_text" TEXT,

    CONSTRAINT "cultures_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "goods" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "plural" TEXT NOT NULL,
    "value" INTEGER NOT NULL,
    "weight" INTEGER NOT NULL,
    "is_food" BOOLEAN NOT NULL,
    "morale_bonus" INTEGER NOT NULL,

    CONSTRAINT "goods_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "kingdoms" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    "ruler_title" TEXT NOT NULL,
    "culture" TEXT NOT NULL,
    "primary_banner_color" TEXT NOT NULL,
    "secondary_banner_color" TEXT NOT NULL,
    "label_color" TEXT NOT NULL,
    "color_1" TEXT NOT NULL,
    "color_2" TEXT NOT NULL,
    "alternative_color_1" TEXT NOT NULL,
    "alternative_color_2" TEXT NOT NULL,
    "desc_text" TEXT NOT NULL,

    CONSTRAINT "kingdoms_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "lords" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "culture" TEXT NOT NULL,
    "default_group" TEXT NOT NULL,
    "age" INTEGER NOT NULL,
    "sex" TEXT NOT NULL,

    CONSTRAINT "lords_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "mounts" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "culture" TEXT NOT NULL,
    "subtype" TEXT NOT NULL,
    "difficulty" INTEGER NOT NULL,
    "is_merchandise" BOOLEAN NOT NULL,
    "maneuver" INTEGER NOT NULL,
    "speed" INTEGER NOT NULL,
    "charge_damage" INTEGER NOT NULL,
    "health" INTEGER NOT NULL,

    CONSTRAINT "mounts_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "towns" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "owner_id" TEXT NOT NULL,
    "owner_name" TEXT NOT NULL,
    "culture" TEXT NOT NULL,
    "x_position" DOUBLE PRECISION NOT NULL,
    "y_position" DOUBLE PRECISION NOT NULL,
    "prosperity" INTEGER NOT NULL,
    "wall_level" INTEGER NOT NULL,
    "bound_village_1" TEXT NOT NULL,
    "bound_village_2" TEXT NOT NULL,
    "bound_village_3" TEXT,
    "bound_village_4" TEXT,
    "desc_text" TEXT NOT NULL,

    CONSTRAINT "towns_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "troops" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "culture" TEXT NOT NULL,
    "default_group" TEXT NOT NULL,
    "occupation" TEXT NOT NULL,
    "level" INTEGER NOT NULL,
    "upgrade_target_1" TEXT,
    "upgrade_target_2" TEXT,
    "one_handed" INTEGER NOT NULL,
    "two_handed" INTEGER NOT NULL,
    "polearm" INTEGER NOT NULL,
    "bow" INTEGER NOT NULL,
    "crossbow" INTEGER NOT NULL,
    "throwing" INTEGER NOT NULL,
    "riding" INTEGER NOT NULL,
    "athletics" INTEGER NOT NULL,

    CONSTRAINT "troops_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "villages" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "culture" TEXT NOT NULL,
    "village_type" TEXT NOT NULL,
    "x_position" DOUBLE PRECISION NOT NULL,
    "y_position" DOUBLE PRECISION NOT NULL,
    "hearth" INTEGER NOT NULL,
    "bound_settlement" TEXT NOT NULL,

    CONSTRAINT "villages_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "armors_name_key" ON "armors"("name");

-- CreateIndex
CREATE UNIQUE INDEX "bows_name_key" ON "bows"("name");

-- CreateIndex
CREATE UNIQUE INDEX "castles_name_key" ON "castles"("name");

-- CreateIndex
CREATE UNIQUE INDEX "clans_name_key" ON "clans"("name");

-- CreateIndex
CREATE UNIQUE INDEX "cultures_name_key" ON "cultures"("name");

-- CreateIndex
CREATE UNIQUE INDEX "goods_name_key" ON "goods"("name");

-- CreateIndex
CREATE UNIQUE INDEX "kingdoms_name_key" ON "kingdoms"("name");

-- CreateIndex
CREATE UNIQUE INDEX "lords_name_key" ON "lords"("name");

-- CreateIndex
CREATE UNIQUE INDEX "mounts_name_key" ON "mounts"("name");

-- CreateIndex
CREATE UNIQUE INDEX "towns_name_key" ON "towns"("name");

-- CreateIndex
CREATE UNIQUE INDEX "troops_name_key" ON "troops"("name");

-- CreateIndex
CREATE UNIQUE INDEX "villages_name_key" ON "villages"("name");
